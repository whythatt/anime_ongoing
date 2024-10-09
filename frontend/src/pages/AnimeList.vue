<script setup>
import { inject, ref, onMounted, watch } from 'vue'
import axios from 'axios'

import AnimeCard from '../components/AnimeCard.vue'
import Filters from '../components/Filters.vue'

const filters = inject('filters')

const animes = ref([]) // Все аниме
const displayedAnimes = ref([]) // Аниме, которые будут отображаться
const limit = 48 // Количество загружаемых аниме за раз
const currentCount = ref(0) // Количество уже загруженных аниме
const hasMore = ref(true) // Флаг для проверки наличия дополнительных данных

const favorites = ref([])

// для того чтобы кнопка загружалась последней
const dataLoaded = ref(false)
onMounted(() => {
  setTimeout(() => {
    dataLoaded.value = true // Устанавливаем флаг, когда данные загружены
  }, 2000) // Задержка в 2 секунды для демонстрации
})

const fetchAnimes = async () => {
  try {
    const params = {
      filter: filters.filter,
      search: filters.search || ''
    }

    const { data } = await axios.get('http://127.0.0.1:8000/api/animes/', {
      params
    })

    animes.value = data.map((obj) => ({
      ...obj,
      isFavorite: false,
      favoriteId: null
    }))

    currentCount.value = 0
    displayedAnimes.value = [] // Очищаем отображаемые аниме
    loadMore() // Загружаем первые 48 аниме
  } catch (err) {
    console.log(err)
  }
}

const loadMore = () => {
  const nextBatch = animes.value.slice(currentCount.value, currentCount.value + limit)

  if (nextBatch.length > 0) {
    displayedAnimes.value.push(...nextBatch) // Добавляем новые аниме к отображаемым
    currentCount.value += nextBatch.length // Увеличиваем количество загруженных аниме

    // Проверяем наличие дополнительных данных для загрузки
    hasMore.value = currentCount.value < animes.value.length
  }
  fetchFavorites() // перепроверяю какие аниме в избранном
}

const fetchFavorites = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    } else {
      const { data: favs } = await axios.get('http://localhost:8000/api/favorites/', {
        headers: { Authorization: `JWT ${accessToken}` }
      })
      favorites.value = favs
      displayedAnimes.value = displayedAnimes.value.map((anime) => {
        const favorite = favs.find((favorite) => favorite.anime.id === anime.id)

        if (!favorite) {
          return anime
        }

        return {
          ...anime,
          isFavorite: true,
          favoriteId: favorite.id
        }
      })
    }
  } catch (err) {
    console.log(err)
  }
}

const changeFavorites = async (anime) => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }
    const obj = { anime_id: anime.id, anime }

    if (!anime.isFavorite) {
      const { data } = await axios.post('http://localhost:8000/api/favorites/', obj, {
        headers: { Authorization: `JWT ${accessToken}` }
      })

      anime.isFavorite = true
      anime.favoriteId = data.id
    } else {
      await axios.delete(`http://localhost:8000/api/favorites/${anime.favoriteId}/`, {
        headers: { Authorization: `JWT ${accessToken}` }
      })
      anime.isFavorite = false
      anime.favoriteId = null
    }
  } catch (err) {
    console.error('Ошибка при добавлении/удалении закладки', err)
  }
}

onMounted(async () => {
  await fetchAnimes(), await fetchFavorites()
})
watch(
  filters,
  async () => {
    await fetchAnimes()
    await fetchFavorites()
  },
  { deep: true }
)
</script>

<template>
  <Filters pageName="Anime list" />

  <div class="anime-list" v-auto-animate>
    <AnimeCard
      v-for="anime in displayedAnimes"
      :key="anime.id"
      :id="anime.id"
      :title="anime.title"
      :picName="anime.pic_name"
      :nextEpisodeCount="anime.next_episode_count"
      :totalEpisodes="anime.total_episodes"
      :releaseDateNextEp="anime.release_date_next_ep"
      :mediatype="anime.mediatype"
      :season="anime.season"
      :releaseDate="anime.release_date"
      :status="anime.status"
      :episodeDuration="anime.episode_duration"
      :score="anime.score"
      :description="anime.description"
      :onClickFavorite="() => changeFavorites(anime)"
      :isFavorite="anime.isFavorite"
    />
  </div>
  <button class="load-more" v-if="hasMore && dataLoaded && currentCount > 0" @click="loadMore">
    <svg viewBox="0 0 24 24" fill="none" width="36" xmlns="http://www.w3.org/2000/svg">
      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
      <g id="SVGRepo_iconCarrier">
        <path
          d="M12 6.5L12 17.5M12 17.5L16 12.9118M12 17.5L8 12.9118"
          stroke="#FFDBB7"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        ></path>
      </g>
    </svg>
  </button>
  <span class="nothing-found" v-if="dataLoaded && currentCount == 0">Nothing found</span>
</template>

<style scoped>
.anime-list {
  max-width: 1340px;
  margin: 0 auto;
  padding: 0 30px;
  display: grid;
  grid-gap: 15px 25px;
  grid-template-columns: repeat(auto-fill, 185px);
  justify-content: space-between;
  margin-bottom: 40px;
}

.load-more {
  display: block;
  margin: 0 auto 30px auto;
  font-size: 18px;
  background-color: #748c3a;
  padding: 7px 7px;
  border-radius: 50%;
}

.nothing-found {
  opacity: 0.7;
  display: block;
  margin: 0 auto 30px auto;
  font-size: 24px;
  width: fit-content;
}

@media (max-width: 1540px) {
  .anime-list {
    max-width: 1140px;
  }
}

@media (max-width: 1085px) {
  .anime-list {
    grid-template-columns: repeat(auto-fill, minmax(125px, 1fr));
  }
}

@media (max-width: 484px) {
  .anime-img {
    height: 100%;
  }
}
</style>

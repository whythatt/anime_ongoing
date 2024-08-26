<script setup>
import { inject, ref, onMounted, watch } from 'vue'
import axios from 'axios'

import AnimeCard from '../components/AnimeCard.vue'
import Filters from '../components/Filters.vue'

const filters = inject('filters')

const animes = ref([])
const favorites = ref([])

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
  } catch (err) {
    console.log(err)
  }
}

const fetchFavorites = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }

    const { data: favs } = await axios.get('http://localhost:8000/api/favorites/', {
      headers: { Authorization: `JWT ${accessToken}` }
    })
    favorites.value = favs
    animes.value = animes.value.map((anime) => {
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
      v-for="anime in animes"
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
</template>

<style scoped>
.anime-list {
  width: 1304px;
  margin: 0 auto;
  display: grid;
  grid-gap: 25px 20px;
  grid-template-columns: repeat(auto-fill, 185px);
  justify-content: space-between;
  margin-bottom: 50px;
}
</style>

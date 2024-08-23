<script setup>
import { onMounted, ref, inject, watch } from 'vue'
import axios from 'axios'

import AnimeCard from '../components/AnimeCard.vue'

const favorites = ref([])

const fetchFavorites = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }

    const { data } = await axios.get('http://localhost:8000/api/favorites/', {
      headers: { Authorization: `JWT ${accessToken}` }
    })

    favorites.value = data.map((obj) => ({
      ...obj,
      isFavorite: true
    }))

    console.log(favorites.value)
  } catch (err) {
    console.log(err)
  }
}

const changeFavorites = async (favorite) => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }
    const obj = { anime_id: favorite.anime.id }

    if (!favorite.isFavorite) {
      const { data } = await axios.post('http://localhost:8000/api/favorites/', obj, {
        headers: { Authorization: `JWT ${accessToken}` }
      })

      favorite.isFavorite = true
    } else {
      await axios.delete(`http://localhost:8000/api/favorites/${favorite.id}/`, {
        headers: { Authorization: `JWT ${accessToken}` }
      })
      favorite.isFavorite = false
    }
  } catch (err) {
    console.error('Ошибка при добавлении/удалении закладки', err)
  }
}

onMounted(() => fetchFavorites())
</script>

<template>
  <div class="title-block">Favorites list</div>
  <div class="favorites-list" v-auto-animate>
    <AnimeCard
      v-for="fav in favorites"
      :key="fav.anime.id"
      :id="fav.anime.id"
      :title="fav.anime.title"
      :picName="fav.anime.pic_name"
      :nextEpisodeCount="fav.anime.next_episode_count"
      :totalEpisodes="fav.anime.total_episodes"
      :releaseDateNextEp="fav.anime.release_date_next_ep"
      :mediatype="fav.anime.mediatype"
      :season="fav.anime.season"
      :releaseDate="fav.anime.release_date"
      :status="fav.anime.status"
      :episodeDuration="fav.anime.episode_duration"
      :score="fav.anime.score"
      :isFavorite="fav.isFavorite"
      :onClickFavorite="() => changeFavorites(fav)"
      :description="fav.anime.description"
    />
  </div>
</template>

<style scoped>
.title-block {
  font-size: 23px;
  width: 1304px;
  margin: 0 auto 32px auto;
}

.favorites-list {
  width: 1304px;
  margin: 0 auto;
  display: grid;
  grid-gap: 25px 20px;
  grid-template-columns: repeat(auto-fill, 185px);
  justify-content: space-between;
  margin-bottom: 50px;
}
</style>

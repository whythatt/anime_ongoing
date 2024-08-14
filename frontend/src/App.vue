<script setup>
import { onMounted, reactive, ref, watch, provide } from 'vue'
import axios from 'axios'
import debounce from 'lodash.debounce'

import Header from './components/Header.vue'

const animes = ref([])
const favorites = ref([])

const filters = reactive({
  filter: '',
  search: ''
})

const onChangeSelect = (event) => {
  filters.filter = event.target.value
}
const onChangeInput = debounce((event) => {
  filters.search = event.target.value
}, 300)

const fetchAnimes = async () => {
  try {
    const params = {
      filter: filters.filter
    }

    if (filters.search) {
      params.search = `${filters.search}`
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

const addToFavorite = async (anime) => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }
    const obj = { anime_id: anime.id }

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

const fetchFavorites = async () => {
  try {
    const accessToken = localStorage.getItem('accessToken')
    if (!accessToken) {
      console.warn('Токен доступа отсутствует')
    }

    const { data } = await axios.get('http://localhost:8000/api/favorites/', {
      headers: { Authorization: `JWT ${accessToken}` }
    })

    favorites.value = data
    animes.value.forEach((anime) => {
      const isFavorite = favorites.value.some((favorite) => favorite.anime === anime.id)
      anime.isFavorite = isFavorite
    })
  } catch (err) {
    console.log(err)
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

provide('filters', { filters, onChangeSelect, onChangeInput })
provide('animes', { animes, fetchAnimes })
provide('favorites', { favorites, fetchFavorites })
provide('addToFavorite', addToFavorite)
</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
  <Header />
  <RouterView />
</template>

<style></style>

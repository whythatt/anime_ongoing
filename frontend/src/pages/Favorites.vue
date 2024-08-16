<script setup>
import { onMounted, ref, watch, inject } from 'vue'
import axios from 'axios'

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

    console.log(data)
  } catch (err) {
    console.log(err)
  }
}

onMounted(() => fetchFavorites())
</script>

<template>
  <h1>Favorites</h1>
  <div v-for="fav in favorites" :key="fav.id">
    {{ fav }}
  </div>
  <span @click="sosiHui">Click here</span>
</template>

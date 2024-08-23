<script setup>
import { onMounted, reactive, ref, watch, provide } from 'vue'
import axios from 'axios'

const animes = ref([])

const fetchAnimes = async () => {
  try {
    const { data } = await axios.get('http://127.0.0.1:8000/api/animes/')

    animes.value = data.map((obj) => ({
      ...obj,
      isFavorite: false,
      favoriteId: null
    }))
  } catch (err) {
    console.log(err)
  }
}
</script>

<template></template>

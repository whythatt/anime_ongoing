<script setup>
import { onMounted, reactive, ref, watch } from 'vue'
import axios from 'axios'

import Header from './components/Header.vue'
import AnimeCardList from './components/AnimeCardList.vue'

const animes = ref([])

const filters = reactive({
  filter: '',
  search: ''
})

const onChangeSelect = (event) => {
  filters.filter = event.target.value
}
const onChangeInput = (event) => {
  filters.search = event.target.value
}

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

    animes.value = data
  } catch (err) {
    console.log(err)
  }
}

onMounted(fetchAnimes)
watch(filters, fetchAnimes)
</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
  <Header />
  <div id="main">
    <div id="anime-list-h2" class="flex flex-row justify-between mb-5">
      <h2 class="text-2xl text-blue-400">Anime list</h2>
      <div class="flex gap-x-3">
        <select @change="onChangeSelect" class="focus:outline-none rounded-xl px-2" id="select">
          <option value="">All</option>
          <option value="tv">TV</option>
          <option value="movie">Movie</option>
          <option value="ongoing">Ongoing</option>
          <option value="delayed">Delayed</option>
          <option value="upcoming">Upcoming</option>
        </select>
        <input
          @input="onChangeInput"
          id="search"
          class="focus:outline-none rounded-xl px-3 py-2"
          type="text"
          placeholder="Search.."
        />
      </div>
    </div>
    <AnimeCardList :animes="animes" />
  </div>
</template>

<style scoped>
#main {
  width: 1022px;
  margin: 40px auto 40px auto;
}

#anime-list-h2 {
  color: #c5c5c5;
}

#search {
  width: 208px;
  height: 35px;
  background-color: #2f2f2f;
}

#select {
  font-size: 15px;
  width: 150px;
  height: 35px;
  background-color: #2f2f2f;
}
</style>

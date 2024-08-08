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
  <div class="main">
    <div class="title-block">
      <span>Anime list</span>
      <div class="filters">
        <select @change="onChangeSelect">
          <option value="">All</option>
          <option value="tv">TV</option>
          <option value="movie">Movie</option>
          <option value="ongoing">Ongoing</option>
          <option value="delayed">Delayed</option>
          <option value="upcoming">Upcoming</option>
        </select>
        <input @input="onChangeInput" type="text" placeholder="Search.." />
      </div>
    </div>
    <AnimeCardList :animes="animes" />
  </div>
</template>

<style scoped>
.main {
  width: 1304px;
  margin: 0 auto;
}

.title-block {
  display: flex;
  justify-content: space-between;
  margin-bottom: 32px;
}
.title-block span {
  font-size: 23px;
}

input,
select {
  height: 35px;
  border-radius: 5px;
  outline: none;
  background-color: rgba(206, 255, 208, 0.4);
  font-size: 15px;
}

select {
  width: 120px;
  margin-right: 15px;
  padding-left: 4px;
}

input {
  width: 210px;
  padding-left: 8px;
}
</style>

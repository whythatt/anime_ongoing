<script setup>
import { onMounted, reactive, ref, watch, inject } from 'vue'
import axios from 'axios'
import debounce from 'lodash.debounce'

import AnimeCard from '../components/AnimeCard.vue'

const { filters, onChangeSelect, onChangeInput } = inject('filters')
const { animes, fetchAnimes } = inject('animes')
//const { favorites, fetchFavorites } = inject('favorites')

const addToFavorite = inject('addToFavorite')
</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
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
      :onClickFavorite="() => addToFavorite(anime)"
      :isFavorite="anime.isFavorite"
    />
  </div>
</template>

<style scoped>
.title-block {
  display: flex;
  justify-content: space-between;
  width: 1304px;
  margin: 0 auto 32px auto;
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

<script setup>
import { inject, ref, onMounted, watch } from 'vue'
import axios from 'axios'

import AnimeCard from '../components/AnimeCard.vue'
import Filters from '../components/Filters.vue'
import FetchAnimes from '../components/FetchAnimes.vue'

const { animes, fetchAnimes } = inject('animes')
const { favorites, fetchFavorites } = inject('favorites')
const { filters, onChangeSelect, onChangeInput } = inject('filters')
const changeFavorites = inject('changeFavorites')

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

  <FetchAnimes ref="animesComp" />
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

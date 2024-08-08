<script setup>
import AnimeCard from './AnimeCard.vue'

defineProps({
  animes: Array
})
</script>

<template>
  <div class="anime-list">
    <AnimeCard
      v-for="anime in animes"
      :key="anime.id"
      :title="anime.title"
      :picName="anime.pic_name"
      :totalEpisodes="anime.total_episodes"
      :releaseDateNextEp="anime.release_data_next_ep"
      :mediatype="anime.mediatype"
      :releaseDate="anime.release_date"
      :status="anime.status"
      :episodeDuration="anime.episode_duration"
      :score="anime.score"
      :description="anime.description"
      :isFavorite="false"
    />
  </div>
</template>

<style scoped>
.anime-list {
  display: grid;
  grid-gap: 25px 20px;
  grid-template-columns: repeat(auto-fill, 185px);
  justify-content: space-between;
  margin-bottom: 50px;
}
</style>

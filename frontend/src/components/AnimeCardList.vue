<script setup>
import AnimeCard from './AnimeCard.vue'

defineProps({
  animes: Array
})
</script>

<template>
  <div id="animes" class="flex flex-wrap gap-x-6 gap-y-8">
    <AnimeCard
      v-for="anime in animes"
      :key="anime.id"
      :title="anime.title"
      :pic_name="anime.pic_name"
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

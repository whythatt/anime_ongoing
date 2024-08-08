<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: String,
  picName: String,
  totalEpisodes: Number,
  releaseDateNextEp: String,
  mediatype: String,
  releaseDate: String,
  status: String,
  episodeDuration: String,
  score: Number,
  description: String,
  isFavorite: Boolean
})
</script>

<template>
  <div class="anime-card">
    <div class="anime-img">
      <img :src="picName" alt="" />
    </div>
    <div class="anime-title">
      {{ title }}
    </div>
  </div>
</template>

<style>
.anime-card {
  cursor: pointer;
}
.anime-card:hover {
  color: #049548;
  transition: all 0.3s linear;
}

.anime-img {
  width: 185px;
  height: 265px;
  margin-bottom: 5px;
  border-radius: 5px;
  box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.2);
}
.anime-img img {
  width: 100%;
  height: 100%;
  border-radius: 5px;
}

.anime-title {
  width: 185px;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.2em;
  max-height: 2.4em;
}
</style>

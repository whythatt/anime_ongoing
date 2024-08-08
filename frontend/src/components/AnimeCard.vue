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
    <div class="info-block"></div>
  </div>
</template>

<style>
.anime-card {
  position: relative;
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
  border-radius: 4px;
  box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.2);
}
.anime-img img {
  width: 100%;
  height: 100%;
  border-radius: 4px;
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

.info-block {
  width: 300px;
  height: 200px;
  background-color: red;
  border-radius: 7px;
  display: none;
  position: absolute;
  z-index: 10;
  top: 7px;
}

.anime-card:hover .info-block {
  display: block;
}
.anime-card:nth-child(6n + 1):hover .info-block,
.anime-card:nth-child(6n + 2):hover .info-block,
.anime-card:nth-child(6n + 3):hover .info-block,
.anime-card:nth-child(6n + 4):hover .info-block {
  margin-left: 18px;
  left: 100%;
}
.anime-card:nth-child(6n + 5):hover .info-block,
.anime-card:nth-child(6n + 6):hover .info-block {
  margin-right: 18px;
  right: 100%;
}
</style>

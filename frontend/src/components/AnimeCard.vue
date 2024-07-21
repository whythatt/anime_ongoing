<script setup>
import { ref } from 'vue'

const props = defineProps({
  title: String,
  imageUrl: String,
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

const showInfoBlock = ref(false)

const showInfo = () => {
  showInfoBlock.value = true
}

const hideInfo = () => {
  showInfoBlock.value = false
}
</script>

<template>
  <div class="main relative">
    <div class="anime" @mouseenter="showInfo" @mouseleave="hideInfo">
      <img
        :src="isFavorite ? '/fill_heart.svg' : '/heart.svg'"
        alt=""
        class="heart-icon drop-shadow"
      />
      <img id="anime-logo" class="rounded-t-xl" :src="imageUrl" />
      <div class="anime-bottom-info rounded-b-xl text-base flex flex-col justify-between px-2 py-1">
        <span>{{ title }}</span>
        <span class="text-gray-400" style="font-size: 11px"
          >{{ mediatype }} - {{ totalEpisodes }} eps</span
        >
      </div>
    </div>
    <div class="info-block" v-if="showInfoBlock">
      <span class="title">{{ title }}</span>
      <div class="icon_info flex gap-2.5">
        <div class="score flex gap-1"><img src="/score.svg" alt="" />{{ score }}</div>
        <div class="mediatype flex gap-1"><img src="/mediatype.svg" alt="" />{{ mediatype }}</div>
        <div class="episodeDuration flex gap-1">
          <img src="/episode_duration.svg" alt="" />{{ episodeDuration }}
        </div>
        <div class="release_date_next_ep flex gap-1">
          <img src="/release_date_next_ep.svg" alt="" />{{ releaseDateNextEp }}
        </div>
      </div>
      <div class="text_info">
        <div class="status">Status: {{ status }}</div>
        <div class="total_episodes">Number of episodes: {{ totalEpisodes }}</div>
        <div class="release_date">Release date: {{ releaseDate }}</div>
      </div>
      <span class="description opacity-70">{{ description }}</span>
    </div>
  </div>
</template>

<style>
.anime-bottom-info {
  background-color: #2f2f2f;
  color: #7cbee3;
  height: 79px;
}

.anime {
  position: relative;
  display: inline-block;
  width: 185px;
  height: 344px;
}

.anime img {
  max-width: 100%;
  height: auto;
}
.heart-icon {
  width: 26px;
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.info-block {
  position: absolute;
  top: 10px;
  left: 105%;
  z-index: 10;
  color: #c5c5c5;
  border-radius: 15px;
  padding: 10px;
  background-color: #2f2f2f;
  width: 356px;
  height: 260px;
  display: flex;
  flex-direction: column;
  row-gap: 10px;
}

.title {
  color: #7cbee3;
  font-size: 18px;
}

.icon_info {
  font-size: 15px;
}

.icon_info img {
  width: 10px;
}

.text_info,
.description {
  font-size: 13px;
}
</style>

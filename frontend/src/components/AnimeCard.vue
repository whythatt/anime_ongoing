<script setup>
import { ref, computed } from 'vue'

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

const showInfo = ref(false)
const isHoveringInfoBlock = ref(false)
const cardRef = ref(null)

const infoBlockPosition = computed(() => {
  if (!cardRef.value) return {}
  const { left, top, width, height } = cardRef.value.getBoundingClientRect()
  return {
    position: 'fixed',
    top: `${top + 52}px`,
    left: `${left + width + 3}px`
  }
})
</script>

<template>
  <div id="card" class="relative">
    <div
      ref="cardRef"
      class="image-container"
      @mouseenter="(showInfo = true), (isHoveringInfoBlock = true)"
      @mouseleave="(showInfo = false), (isHoveringInfoBlock = false)"
    >
      <img
        :src="isFavorite ? '/fill_heart.svg' : '/heart.svg'"
        alt=""
        class="heart-icon drop-shadow"
      />
      <img id="anime-logo" class="rounded-t-xl" :src="imageUrl" />
      <div
        id="anime-bottom-info"
        class="rounded-b-xl text-base flex flex-col justify-between px-2 py-1"
      >
        <span>{{ title }}</span>
        <span class="text-gray-400" style="font-size: 11px"
          >{{ mediatype }} - {{ totalEpisodes }} eps</span
        >
      </div>
    </div>

    <div
      :style="infoBlockPosition"
      class="info_block"
      v-if="showInfo || isHoveringInfoBlock"
      @mouseenter="isHoveringInfoBlock = true"
      @mouseleave="isHoveringInfoBlock = false"
    >
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
      <button class="add_to_favorites">Add to favorites</button>
    </div>
  </div>
</template>

<style>
#anime-bottom-info {
  background-color: #2f2f2f;
  color: #7cbee3;
  height: 79px;
}

#card {
  max-width: 185px;
  max-height: 344px;
  min-width: 185px;
  min-height: 344px;
}

.image-container {
  position: relative;
  display: inline-block;
}

.image-container img {
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

.info_block {
  position: fixed;
  z-index: 1;
  color: #c5c5c5;
  border-radius: 15px;
  padding: 10px;
  background-color: #2f2f2f;
  width: 356px;
  height: 305px;
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

.info_block button {
  background-color: #7cbee3;
  border-radius: 10px;
  color: #1d1d1d;
  font-size: 15px;
  width: 166px;
  height: 37px;
}
.info_block button:hover {
  background-color: #34a8ea;
  transition: all 0.2s linear;
}
</style>

<script setup>
const props = defineProps({
  title: String,
  pic_name: String,
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
  <div id="card" class="">
    <div ref="cardRef" class="image-container">
      <img
        :src="isFavorite ? '/fill_heart.svg' : '/heart.svg'"
        alt=""
        class="heart-icon drop-shadow"
      />
      <img id="anime-logo" class="rounded-t-xl" :src="pic_name" />
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

.title {
  color: #7cbee3;
  font-size: 18px;
}
</style>

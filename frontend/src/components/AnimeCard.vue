<script setup>
import { ref, inject, watch } from 'vue'

const showDetails = ref(false)

const openDetails = () => {
  showDetails.value = true
}
const closeDetails = () => {
  showDetails.value = false
}

const props = defineProps({
  id: Number,
  title: String,
  picName: String,
  nextEpisodeCount: String,
  totalEpisodes: Number,
  releaseDateNextEp: String,
  mediatype: String,
  season: String,
  releaseDate: String,
  status: String,
  episodeDuration: String,
  score: Number,
  description: String,
  updated: Boolean,
  isFavorite: Boolean,
  onClickFavorite: Function
})

const showInfoBlock = ref(false)
const infoBlockPosition = ref('') // Позиция для .info-block

const onMouseEnter = (event) => {
  const cardRect = event.currentTarget.getBoundingClientRect()
  const listRect = document.querySelector('.anime-list').getBoundingClientRect() // Получаем границы .anime-list
  const infoBlockWidth = 294 // Ширина вашего .info-block

  // Проверяем, выходит ли блок за пределы .anime-list
  if (cardRect.right + infoBlockWidth > listRect.right) {
    infoBlockPosition.value = `-${infoBlockWidth + 10}px` // Позиция слева
  } else {
    infoBlockPosition.value = `${cardRect.width + 10}px` // Позиция справа
  }

  showInfoBlock.value = true // Показываем блок
}

const onMouseLeave = () => {
  showInfoBlock.value = false // Скрываем блок
}
</script>

<template>
  <div
    class="anime-card"
    @click="openDetails"
    @mouseenter="onMouseEnter"
    @mouseleave="onMouseLeave"
  >
    <div class="anime-img">
      <img class="anime-pic" :src="picName" alt="" />
      <div class="isUpdated" v-if="updated">NEW</div>
    </div>
    <div class="anime-title">
      {{ title }}
    </div>
    <div
      class="info-block"
      v-if="showInfoBlock"
      @mouseenter="onMouseLeave"
      :style="{ left: infoBlockPosition }"
    >
      <!-- class .next-episode -->
      <div class="next-episode" v-if="nextEpisodeCount && releaseDateNextEp">
        Ep {{ nextEpisodeCount }} will air on {{ releaseDateNextEp }}
      </div>
      <div class="next-episode" v-else-if="nextEpisodeCount">
        Ep {{ nextEpisodeCount }} will air on ?
      </div>
      <div class="next-episode" v-else>Ep ? will air on ?</div>
      <!-- END class .next-episode -->
      <!-- class .score--mediatype--eps -->
      <div class="score--mediatype--eps">
        <div class="score">
          <svg
            style="width: 16px"
            viewBox="0 1 21 21"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            fill="#000000"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <title>star_favorite [#EBCB18]</title>
              <desc>Created with Sketch.</desc>
              <defs></defs>
              <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <g
                  id="Dribbble-Light-Preview"
                  transform="translate(-99.000000, -320.000000)"
                  fill="#D79921"
                >
                  <g id="icons" transform="translate(56.000000, 160.000000)">
                    <path
                      d="M60.556381,172.206 C60.1080307,172.639 59.9043306,173.263 60.0093306,173.875 L60.6865811,177.791 C60.8976313,179.01 59.9211306,180 58.8133798,180 C58.5214796,180 58.2201294,179.931 57.9282291,179.779 L54.3844766,177.93 C54.1072764,177.786 53.8038262,177.714 53.499326,177.714 C53.1958758,177.714 52.8924256,177.786 52.6152254,177.93 L49.0714729,179.779 C48.7795727,179.931 48.4782224,180 48.1863222,180 C47.0785715,180 46.1020708,179.01 46.3131209,177.791 L46.9903714,173.875 C47.0953715,173.263 46.8916713,172.639 46.443321,172.206 L43.575769,169.433 C42.4480682,168.342 43.0707186,166.441 44.6289197,166.216 L48.5916225,165.645 C49.211123,165.556 49.7466233,165.17 50.0227735,164.613 L51.7951748,161.051 C52.143775,160.35 52.8220755,160 53.499326,160 C54.1776265,160 54.855927,160.35 55.2045272,161.051 L56.9769285,164.613 C57.2530787,165.17 57.7885791,165.556 58.4080795,165.645 L62.3707823,166.216 C63.9289834,166.441 64.5516338,168.342 63.423933,169.433 L60.556381,172.206 Z"
                      id="star_favorite-[#EBCB18]"
                    ></path>
                  </g>
                </g>
              </g>
            </g>
          </svg>
          <span style="opacity: 0.7" v-if="score">{{ score }}</span>
          <span style="opacity: 0.7" v-else>0.00</span>
        </div>
        <div class="eps--mediatype" v-if="totalEpisodes || mediatype">
          <svg
            style="width: 19px"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            stroke="#458588"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill="#458588"
                d="M3 17V9a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"
              ></path>
              <path
                stroke="#458588"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 7h7a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h7zm0 0L8 3m4 4 4-4"
              ></path>
            </g>
          </svg>
          <span style="opacity: 0.7" v-if="totalEpisodes"
            >{{ mediatype }} • {{ totalEpisodes }} episodes</span
          >
          <span style="opacity: 0.7" v-else>{{ mediatype }} • ? episodes</span>
        </div>
      </div>
      <!-- end class .score--mediatype--eps -->
      <!-- class .circle-info -->
      <div class="circle-info">
        <div class="status" v-if="status">{{ status }}</div>
        <div class="episodeDuration" v-if="episodeDuration">duration {{ episodeDuration }}</div>
      </div>
      <div class="season">{{ season }}</div>
    </div>
    <teleport to="body" v-if="showDetails">
      <div class="block-details">
        <div class="details-bg" @click="closeDetails"></div>
        <div class="details">
          <div class="img-block">
            <img class="anime-pic" :src="picName" alt="" />
            <button class="add-favorite-button" v-if="!isFavorite" @click="onClickFavorite">
              <svg
                fill="#FFDBB7"
                viewBox="-1 1 19 19"
                xmlns="http://www.w3.org/2000/svg"
                class="cf-icon-svg"
                width="18px"
              >
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path
                    d="m12.673 10.779.798 4.02c.221 1.11-.407 1.566-1.395 1.013L8.5 13.81l-3.576 2.002c-.988.553-1.616.097-1.395-1.013l.397-2.001.401-2.02-1.51-1.397-1.498-1.385c-.832-.769-.592-1.507.532-1.64l2.026-.24 2.044-.242 1.717-3.722c.474-1.028 1.25-1.028 1.724 0l1.717 3.722 2.044.242 2.026.24c1.124.133 1.364.871.533 1.64L14.184 9.38z"
                  ></path>
                </g>
              </svg>
              <span>Add</span>
            </button>
            <button class="remove-favorite-button" v-else @click="onClickFavorite">
              <svg
                fill="#FFDBB7"
                viewBox="-1 1 19 19"
                xmlns="http://www.w3.org/2000/svg"
                class="cf-icon-svg"
                width="18px"
              >
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path
                    d="m12.673 10.779.798 4.02c.221 1.11-.407 1.566-1.395 1.013L8.5 13.81l-3.576 2.002c-.988.553-1.616.097-1.395-1.013l.397-2.001.401-2.02-1.51-1.397-1.498-1.385c-.832-.769-.592-1.507.532-1.64l2.026-.24 2.044-.242 1.717-3.722c.474-1.028 1.25-1.028 1.724 0l1.717 3.722 2.044.242 2.026.24c1.124.133 1.364.871.533 1.64L14.184 9.38z"
                  ></path>
                </g>
              </svg>
              <span>Remove</span>
            </button>
          </div>
          <div class="text-details">
            <div class="full-title">{{ title }}</div>
            <div class="line"></div>
            <div class="description">{{ description }}</div>
          </div>
        </div>
      </div>
    </teleport>
  </div>
</template>

<style>
.block-details {
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.details {
  width: 792px;
  height: fit-content;
  padding: 30px;
  background: rgba(255, 250, 245, 0.68);
  border-radius: 5px;
  backdrop-filter: blur(9px);
  display: flex;
  column-gap: 22px;

  animation-duration: 0.2s;
  animation-name: appear-details;
  animation-timing-function: quartic;
}
@keyframes appear-details {
  0% {
    scale: 0.94;
  }
  100% {
    scale: 1;
  }
}

.details-bg {
  background: rgba(0, 0, 0, 0.3);
  position: fixed;
  width: 100vw;
  height: 100vh;
  animation-duration: 0.3s;
  animation-name: appear-details-bg;
  animation-timing-function: quartic;
}
@keyframes appear-details-bg {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.anime-card {
  position: relative;
  cursor: pointer;
}
.anime-card:hover {
  color: #748c3a;
  transition: all 0.3s linear;
}

.anime-img {
  width: 185px;
  height: 265px;
  margin-bottom: 5px;
  border-radius: 4px;
  box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.2);
  position: relative;
}

.anime-pic {
  width: 100%;
  height: 100%;
  border-radius: 4px;
}

.img-block {
  position: relative;
  width: 199px;
  height: 285px;
  display: flex;
  justify-content: center;
}

.add-favorite-button,
.remove-favorite-button {
  position: absolute;
  bottom: 10px;
  display: flex;
  color: #ffdbb7;
  width: 106px;
  height: 31px;
  font-size: 15px;
  background: rgba(69, 133, 136, 0.7);
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.67);
  border-radius: 4px;
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 4px;
  backdrop-filter: blur(5px);
}

.remove-favorite-button {
  background: rgba(214, 93, 14, 0.7);
}

.text-details {
  margin-top: 10px;
  width: 512px;
  min-height: 222px;
  height: fit-content;
  display: flex;
  flex-direction: column;
  row-gap: 13px;
}

.full-title {
  font-size: 20px;
}

.line {
  width: 100%;
  border: solid #634b36 1px;
}

.description {
  font-size: 14px;
  font-weight: 300;
}

.isUpdated {
  color: #634b36;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 204, 83, 0.8);
  border-radius: 4px;
  width: 90px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.67);
  backdrop-filter: blur(2px);
  position: absolute;
  right: 7px;
  top: 7px;
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
  width: 294px;
  height: 154px;
  padding: 14px;
  background-color: #fffaf5;
  border-radius: 6px;
  box-shadow: 0px 0px 11px rgba(0, 0, 0, 0.2);
  color: #634b36;
  display: none;
  position: absolute;
  z-index: 13;
  top: 8px;

  animation-duration: 0.2s;
  animation-name: appear;
  animation-timing-function: quartic;
}
@keyframes appear {
  0% {
    scale: 0.94;
  }
  100% {
    scale: 1;
  }
}

.info-block .next-episode {
  margin-bottom: 13px;
}

.anime-card:hover .info-block {
  display: block;
}

.score--mediatype--eps,
.circle-info {
  display: flex;
  column-gap: 16px;
}

.score--mediatype--eps .score,
.score--mediatype--eps .eps--mediatype {
  font-size: 15px;
  display: flex;
  column-gap: 6px;
  align-items: center;
  margin-bottom: 11px;
}

.circle-info .status,
.circle-info .episodeDuration {
  color: #ffdbb7;
  height: 26px;
  width: fit-content;
  padding: 6px 16px;
  border-radius: 60px;
  font-size: 14px;
  display: flex;
  align-items: center;
}
.circle-info .status {
  background: #748c3a;
  text-transform: lowercase;
}
.circle-info .episodeDuration {
  background: #458588;
}

.info-block .season {
  opacity: 0.7;
  margin-top: 15px;
  float: right;
  font-size: 13px;
}

@media (max-width: 1085px) {
  .anime-img {
    width: 100%;
    height: 85%;
  }
  .anime-title {
    width: 100%;
    font-size: 13px;
  }
}

@media (max-width: 484px) {
  .anime-img {
    height: 90%;
  }
}
</style>

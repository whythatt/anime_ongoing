<script setup>
import { ref } from 'vue'

const props = defineProps({
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
  isFavorite: Boolean
})
</script>

<template>
  <div class="anime-card">
    <div class="anime-img">
      <img class="anime-pic" :src="picName" alt="" />
      <img class="favorite-icon" :src="isFavorite ? '/favorite.png' : '/unfavorite.png'" alt="" />
    </div>
    <div class="anime-title">
      {{ title }}
    </div>
    <div class="info-block">
      <!-- class .next-episode -->
      <div class="next-episode" v-if="nextEpisodeCount && releaseDateNextEp">
        Ep {{ nextEpisodeCount }} will air on {{ releaseDateNextEp }}
      </div>
      <div class="next-episode" v-else-if="nextEpisodeCount">
        Ep {{ nextEpisodeCount }} will air on ?
      </div>
      <div class="next-episode" v-else>Ep ? will air on ?</div>
      <!-- class .next-episode -->
      <!-- class .circle-info -->
      <div class="circle-info">
        <div class="score" v-if="score">
          <svg
            style="width: 16px"
            viewBox="0 -0.5 21 21"
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
                  fill="#EBCB18"
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
          <span>{{ score }}</span>
        </div>
        <div class="eps--mediatype" v-if="totalEpisodes || mediatype">
          <svg
            style="width: 17px"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            stroke="#38B6D9"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill="#38B6D9"
                d="M3 17V9a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"
              ></path>
              <path
                stroke="#38B6D9"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 7h7a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h7zm0 0L8 3m4 4 4-4"
              ></path>
            </g>
          </svg>
          <span v-if="totalEpisodes">{{ mediatype }} • {{ totalEpisodes }} episodes</span>
          <span v-else>{{ mediatype }} • ? episodes</span>
        </div>
      </div>
      <!-- class .circle-info -->
      <div class="season">{{ season }}</div>
    </div>
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
  position: relative;
}
.anime-pic {
  width: 100%;
  height: 100%;
  border-radius: 4px;
}
.favorite-icon {
  position: absolute;
  opacity: 90%;
  top: 7px;
  left: 79%;
  width: 30px;
  filter: drop-shadow(0px 0px 10px rgba(163, 163, 163, 0.5));
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
  background-color: #ffffff;
  border-radius: 6px;
  box-shadow: 0px 0px 11px rgba(0, 0, 0, 0.2);
  color: #556358;

  display: none;
  position: absolute;
  z-index: 10;
  top: 12px;
}
.info-block .next-episode {
  margin-bottom: 20px;
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

.circle-info {
  display: flex;
  column-gap: 12px;
}
.circle-info .score,
.circle-info .eps--mediatype {
  height: 26px;
  width: fit-content;
  background-color: rgba(0, 0, 0, 0.1);
  padding: 6px 12px;
  border-radius: 60px;
  font-size: 15px;
  display: flex;
  column-gap: 6px;
  align-items: center;
}

.info-block .season {
  opacity: 70%;
  margin-top: 38px;
  float: right;
  font-size: 15px;
}
</style>

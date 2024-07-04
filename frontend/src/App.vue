<script setup>
import Header from './components/Header.vue'
import AnimeCardList from './components/AnimeCardList.vue'
</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
  <Header />
  <div id="main">
    <div id="anime-list-h2" class="flex flex-row justify-between mb-5">
      <h2 class="text-2xl text-blue-400">Anime list</h2>
      <input
        id="search"
        class="focus:outline-none rounded-xl px-3 py-2"
        type="text"
        placeholder="Search.."
      />
    </div>
    <AnimeCardList />
  </div>
</template>

<style scoped>
#main {
  width: 1022px;
  margin: 40px auto 0 auto;
}

#anime-list-h2 {
  color: #c5c5c5;
}

#search {
  width: 208px;
  height: 35px;
  background-color: #2f2f2f;
}
</style>

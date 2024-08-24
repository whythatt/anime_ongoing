<script setup>
import { inject } from 'vue'
import axios from 'axios'
import debounce from 'lodash.debounce'

const { filters, onChangeSelect, onChangeInput } = inject('filters')

const props = defineProps({
  pageName: String
})
</script>

<template>
  <div class="title-block">
    <span>{{ pageName }}</span>
    <div class="filters">
      <select @change="onChangeSelect">
        <option value="">All</option>
        <option value="tv">TV</option>
        <option value="movie">Movie</option>
        <option value="ongoing">Ongoing</option>
        <option value="delayed">Delayed</option>
        <option value="upcoming">Upcoming</option>
      </select>
      <input @input="onChangeInput" type="text" placeholder="Search.." />
    </div>
  </div>
</template>

<style scoped>
.title-block {
  display: flex;
  justify-content: space-between;
  width: 1304px;
  margin: 0 auto 32px auto;
}
.title-block span {
  font-size: 23px;
}

input,
select {
  height: 35px;
  border-radius: 5px;
  outline: none;
  background-color: rgba(206, 255, 208, 0.4);
  font-size: 15px;
}

select {
  width: 120px;
  margin-right: 15px;
  padding-left: 4px;
}

input {
  width: 210px;
  padding-left: 8px;
}
</style>

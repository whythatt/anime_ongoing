<script setup>
import { inject } from 'vue'
import axios from 'axios'

const filters = inject('filters')
const onChangeSelect = inject('onChangeSelect')
const onChangeInput = inject('onChangeInput')

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
  max-width: 1340px;
  padding: 0 30px;
  margin: 0 auto 32px auto;
}
.title-block span {
  font-size: 23px;
}

@media (max-width: 1540px) {
  .title-block {
    max-width: 1140px;
  }
}

input,
select {
  height: 35px;
  border-radius: 5px;
  outline: none;
  background-color: rgba(40, 28, 21, 0.1);
  font-size: 15px;
}
::placeholder {
  color: #634b36;
  opacity: 0.4;
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

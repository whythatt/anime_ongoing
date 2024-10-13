<script setup>
import { onMounted, reactive, ref, watch, provide } from 'vue'
import debounce from 'lodash.debounce'

import Header from './components/Header.vue'

const filters = reactive({
  filter: '',
  search: ''
})

const onChangeSelect = (event) => {
  filters.filter = event.target.value
}

const onChangeInput = debounce((event) => {
  filters.search = event.target.value
}, 300)

provide('filters', filters)
provide('onChangeSelect', onChangeSelect)
provide('onChangeInput', onChangeInput)
</script>

<template>
  <Header />
  <RouterView />
</template>

<style></style>

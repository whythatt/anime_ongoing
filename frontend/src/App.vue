<script setup>
import { onMounted, reactive, ref, watch, provide } from 'vue'
import axios from 'axios'
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
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Document</title>
    </head>
    <body>
      <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
      <Header />
      <RouterView />
    </body>
  </html>
</template>

<style></style>

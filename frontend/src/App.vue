<script setup>
import { provide } from 'vue'
import Header from './components/Header.vue'

const sosiHui = () => {
  alert('vivalivay')
}

provide('sosi', sosiHui)
</script>

<template>
  <link href="https://fonts.googleapis.com/css?family=Lexend Deca" rel="stylesheet" />
  <Header />
  <RouterView />
</template>

<style></style>

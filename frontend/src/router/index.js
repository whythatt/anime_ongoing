import { createRouter, createWebHistory } from 'vue-router'
import AnimeCardList from '../components/AnimeCardList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'animeCardList',
      component: AnimeCardList
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../components/Login.vue')
    }
  ]
})

export default router

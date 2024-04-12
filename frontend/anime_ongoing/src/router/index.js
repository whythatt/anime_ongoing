import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Login.vue'
import UserInfo from '@/components/UserInfo.vue'
import AnimeList from '@/components/AnimeList.vue'
import FavoritesList from '@/components/FavoritesList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/userInfo',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/animeList',
      name: 'AnimeList',
      component: AnimeList
    },
    {
      path: '/favoritesList',
      name: 'FavoritesList',
      component: FavoritesList
    },
  ]
})

export default router

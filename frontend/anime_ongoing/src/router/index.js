import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Login.vue'
import UserInfo from '@/components/UserInfo.vue'
import AnimeList from '@/components/AnimeList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/userinfo',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/animelist',
      name: 'AnimeList',
      component: AnimeList
    },
  ]
})

export default router

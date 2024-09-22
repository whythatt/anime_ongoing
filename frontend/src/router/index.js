import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'animelist',
      component: () => import('../pages/AnimeList.vue')
    },
    {
      path: '/favorites',
      name: 'favorites',
      component: () => import('../pages/Favorites.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../pages/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import('../pages/SignUp.vue')
    },
    {
      path: '/forgot',
      name: 'ForgotPassword',
      component: () => import('../pages/ForgotPassword.vue')
    },
    {
      path: '/reset-password/:uid/:token',
      name: 'ResetPassword',
      component: () => import('../pages/ResetPassword.vue')
    }
  ]
})

export default router

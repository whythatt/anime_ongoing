import './assets/main.css'

import { createApp } from 'vue'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
import axios from 'axios'

import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.use(autoAnimatePlugin)
app.mount('#app')

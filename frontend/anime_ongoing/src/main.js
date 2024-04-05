import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import UserInfo from './components/UserInfo.vue'

const app = createApp(App)

app.use(router)

// app.component('user-info', UserInfo)

app.mount('#app')

// axios.js
import axios from 'axios'
import { checkTokens } from '../services/auth' // Импортируйте вашу функцию проверки токенов

const instance = axios.create({
  baseURL: 'http://localhost:8000' // Укажите базовый URL вашего API
})

// Добавьте интерсептор запроса
instance.interceptors.request.use(
  async (config) => {
    await checkTokens() // Выполните проверку токенов перед каждым запросом
    return config // Возвратите конфигурацию запроса
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default instance

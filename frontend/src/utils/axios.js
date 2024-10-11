// axios.js
import axios from 'axios'
import { refreshAccessToken, checkTokens } from '../services/auth' // Импортируйте вашу функцию проверки токенов

const instance = axios.create({
  baseURL: 'http://localhost:8000' // Укажите базовый URL вашего API
})

// Добавьте интерсептор запроса
instance.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem('accessToken')

    if (accessToken) {
      config.headers.Authorization = `JWT ${accessToken}`
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Интерсептор запроса
instance.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const originalRequest = error.config

    // Проверяем, истек ли токен (401 ошибка)
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true // Устанавливаем флаг, чтобы избежать зацикливания

      try {
        const newAccessToken = await checkTokens() // Обновляем токен
        originalRequest.headers['Authorization'] = `JWT ${newAccessToken}` // Добавляем новый токен в запрос

        return instance(originalRequest) // Повторяем оригинальный запрос с новым токеном
      } catch (refreshError) {
        console.error('Не удалось обновить токен:', refreshError)
        // Здесь можно перенаправить пользователя на страницу логина или выполнить другие действия
      }
    }

    return Promise.reject(error)
  }
)

export default instance

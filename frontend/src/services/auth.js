import { ref } from 'vue'
import axios from '../utils/axios'

const accessToken = ref(localStorage.getItem('accessToken') || '')
const refreshToken = ref(localStorage.getItem('refreshToken') || '')
const ACCESS_TOKEN_EXPIRY = 5 * 60 * 1000 // 1 минут в миллисекундах
const REFRESH_TOKEN_EXPIRY = 24 * 60 * 60 * 1000 // 1 день в миллисекундах

const errorMessage = ref('')

const login = async (email, password) => {
  try {
    const response = await axios.post('/auth/jwt/create', {
      email,
      password
    })

    // Save JWT token
    accessToken.value = response.data.access
    refreshToken.value = response.data.refresh
    localStorage.setItem('accessToken', accessToken.value)
    localStorage.setItem('refreshToken', refreshToken.value)
    localStorage.setItem('accessToken_expiry', getCurrentTime() + ACCESS_TOKEN_EXPIRY)
    localStorage.setItem('refreshToken_expiry', getCurrentTime() + REFRESH_TOKEN_EXPIRY)

    // redirect
    window.location.href = '/'
  } catch (err) {
    // Обработка ошибки
    if (err.response && err.response.status === 401) {
      errorMessage.value = 'Incorrect email or password' // Устанавливаем сообщение об ошибке
    }
    console.error(err)
  }
}

const signUp = async (username, email, password, re_password) => {
  try {
    const response = await axios.post('/auth/users/', {
      username,
      email,
      password,
      re_password
    })

    // redirect
    window.location.href = '/login'
  } catch (err) {
    console.error(err)
  }
}

const logout = () => {
  accessToken.value = ''
  refreshToken.value = ''
  localStorage.removeItem('accessToken')
  localStorage.removeItem('refreshToken')

  // redirect
  window.location.href = '/'
}

const getCurrentTime = () => new Date().getTime()
// Проверка действительности access token
const isAccessTokenValid = () => {
  const expiryTime = localStorage.getItem('accessToken_expiry')

  return accessToken && expiryTime && getCurrentTime() < expiryTime
}

// Проверка действительности refresh token
const isRefreshTokenValid = () => {
  const expiryTime = localStorage.getItem('refreshToken_expiry')

  return refreshToken && expiryTime && getCurrentTime() < expiryTime
}

// Функция для обновления access token
const refreshAccessToken = async () => {
  if (!isRefreshTokenValid()) {
    // Удаляем токены, если refresh token недействителен
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    return null
  }

  try {
    const response = await axios.post('/auth/jwt/refresh/', {
      refresh: refreshToken.value
    })

    const data = response.data

    // Сохраняем новый access token и его время жизни
    localStorage.setItem('accessToken', data.access)
    localStorage.setItem('accessToken_expiry', getCurrentTime() + ACCESS_TOKEN_EXPIRY)

    return data.accessToken
  } catch (error) {
    console.error(error)
  }
}

// Основная функция для проверки токенов перед запросом
const checkTokens = async () => {
  if (isAccessTokenValid()) {
    // Если access token действителен, ничего не делаем
    return
  } else {
    // Если access token недействителен, пробуем обновить его
    const newAccessToken = await refreshAccessToken()

    if (!newAccessToken) {
      console.log('Токены недействительны. Пожалуйста, выполните вход снова.')
      // Здесь можно перенаправить пользователя на страницу входа или показать сообщение
    }
  }
}

export { login, errorMessage, signUp, logout, refreshAccessToken, checkTokens }

import { ref } from 'vue'
import axios from 'axios'

const accessToken = ref(localStorage.getItem('accessToken') || '')
const refreshToken = ref(localStorage.getItem('refreshToken') || '')

const login = async (email, password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/jwt/create', {
      email,
      password
    })

    // Save JWT token
    accessToken.value = response.data.access
    refreshToken.value = response.data.refresh
    localStorage.setItem('accessToken', accessToken.value)
    localStorage.setItem('refreshToken', refreshToken.value)

    // redirect
    window.location.href = '/'
  } catch (err) {
    console.error(err)
  }
}

const signUp = async (username, email, password, re_password) => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/users/', {
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

const refreshAccessToken = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/jwt/refresh/', {
      refresh: refreshToken.value
    })
    accessToken.value = response.data.access
    localStorage.setItem('accessToken', accessToken.value)
  } catch (error) {
    console.error('Refresh token error:', error)
    logout()
  }
}

const checkTokenValidity = () => {
  if (!accessToken.value) {
    return false
  }

  const tokenParts = accessToken.value.split('.')
  if (tokenParts.length !== 3) {
    return false
  }

  try {
    const payload = JSON.parse(atob(tokenParts[1]))
    const now = Math.floor(Date.now() / 1000)
    return now <= payload.exp
  } catch (error) {
    console.error('Token validity error:', error)
    return false
  }
}

export { login, signUp, logout, refreshAccessToken, checkTokenValidity, accessToken, refreshToken }

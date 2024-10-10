<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from '../utils/axios'

const route = useRoute()
const uid = ref(route.params.uid)
const token = ref(route.params.token)
const newPassword = ref('')
const reNewPassword = ref('')
// const isSending = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleReset = async () => {
  if (newPassword.value !== reNewPassword.value) {
    errorMessage.value = "Passwrods don't match."
    return
  }

  // isSending.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    await axios.post('/auth/users/reset_password_confirm/', {
      uid: uid.value,
      token: token.value,
      new_password: newPassword.value,
      re_new_password: reNewPassword.value
    })
    successMessage.value = 'Password successfully saved.'
  } catch (error) {
    errorMessage.value = error.response.data.detail || 'Error when resseting password.'
  }
}
</script>

<template>
  <div class="main">
    <div class="login-logo">
      <svg width="90" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M3.5 9.56757V14.4324C3.5 16.7258 3.5 17.8724 4.22162 18.5849C4.87718 19.2321 5.89572 19.2913 7.81827 19.2968C7.81303 19.262 7.80803 19.2271 7.80324 19.192C7.68837 18.3484 7.68839 17.2759 7.68841 15.9453L7.68841 15.8919C7.68841 15.4889 8.01933 15.1622 8.42754 15.1622C8.83575 15.1622 9.16667 15.4889 9.16667 15.8919C9.16667 17.2885 9.16824 18.2626 9.26832 18.9975C9.36554 19.7114 9.54337 20.0895 9.81613 20.3588C10.0889 20.6281 10.4718 20.8037 11.195 20.8996C11.9394 20.9985 12.926 21 14.3406 21H15.3261C16.7407 21 17.7273 20.9985 18.4717 20.8996C19.1948 20.8037 19.5778 20.6281 19.8505 20.3588C20.1233 20.0895 20.3011 19.7114 20.3983 18.9975C20.4984 18.2626 20.5 17.2885 20.5 15.8919V8.10811C20.5 6.71149 20.4984 5.73743 20.3983 5.0025C20.3011 4.28855 20.1233 3.91048 19.8505 3.6412C19.5778 3.37192 19.1948 3.19635 18.4717 3.10036C17.7273 3.00155 16.7407 3 15.3261 3H14.3406C12.926 3 11.9394 3.00155 11.195 3.10036C10.4718 3.19635 10.0889 3.37192 9.81613 3.6412C9.54337 3.91048 9.36554 4.28855 9.26832 5.0025C9.16824 5.73743 9.16667 6.71149 9.16667 8.10811C9.16667 8.51113 8.83575 8.83784 8.42754 8.83784C8.01933 8.83784 7.68841 8.51113 7.68841 8.10811L7.68841 8.05472C7.68839 6.72409 7.68837 5.65156 7.80324 4.80803C7.80803 4.77288 7.81303 4.73795 7.81827 4.70325C5.89572 4.70867 4.87718 4.76792 4.22162 5.41515C3.5 6.12759 3.5 7.27425 3.5 9.56757ZM13.385 14.9484L15.8487 12.516C16.1374 12.231 16.1374 11.769 15.8487 11.484L13.385 9.05157C13.0963 8.76659 12.6283 8.76659 12.3397 9.05157C12.051 9.33655 12.051 9.79859 12.3397 10.0836L13.5417 11.2703H6.45652C6.04831 11.2703 5.71739 11.597 5.71739 12C5.71739 12.403 6.04831 12.7297 6.45652 12.7297H13.5417L12.3397 13.9164C12.051 14.2014 12.051 14.6635 12.3397 14.9484C12.6283 15.2334 13.0963 15.2334 13.385 14.9484Z"
          fill="#748c3a"
        ></path>
      </svg>
      <span>Forgot</span>
    </div>
    <form @submit.prevent="handleReset">
      <input type="hidden" v-model="uid" />
      <input type="hidden" v-model="token" />
      <div class="password">
        <label for="password">New password</label>
        <div class="password-input">
          <svg
            style="padding-bottom: 4px"
            width="20"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M5.5 10V7C5.5 5.27609 6.18482 3.62279 7.40381 2.40381C8.62279 1.18482 10.2761 0.5 12 0.5C13.7239 0.5 15.3772 1.18482 16.5962 2.40381C17.8152 3.62279 18.5 5.27609 18.5 7V10H19C20.6569 10 22 11.3431 22 13V20C22 21.6569 20.6569 23 19 23H5C3.34315 23 2 21.6569 2 20V13C2 11.3431 3.34315 10 5 10H5.5ZM9.52513 4.52513C10.1815 3.86875 11.0717 3.5 12 3.5C12.9283 3.5 13.8185 3.86875 14.4749 4.52513C15.1313 5.1815 15.5 6.07174 15.5 7V10H8.5V7C8.5 6.07174 8.86875 5.1815 9.52513 4.52513Z"
                fill="#634b36"
              ></path>
            </g>
          </svg>
          <input type="password" placeholder="••••••••••••" v-model="newPassword" required />
        </div>
      </div>
      <div class="password">
        <label for="password">Retype password</label>
        <div class="password-input">
          <svg
            style="padding-bottom: 4px"
            width="20"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <path
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M5.5 10V7C5.5 5.27609 6.18482 3.62279 7.40381 2.40381C8.62279 1.18482 10.2761 0.5 12 0.5C13.7239 0.5 15.3772 1.18482 16.5962 2.40381C17.8152 3.62279 18.5 5.27609 18.5 7V10H19C20.6569 10 22 11.3431 22 13V20C22 21.6569 20.6569 23 19 23H5C3.34315 23 2 21.6569 2 20V13C2 11.3431 3.34315 10 5 10H5.5ZM9.52513 4.52513C10.1815 3.86875 11.0717 3.5 12 3.5C12.9283 3.5 13.8185 3.86875 14.4749 4.52513C15.1313 5.1815 15.5 6.07174 15.5 7V10H8.5V7C8.5 6.07174 8.86875 5.1815 9.52513 4.52513Z"
                fill="#634b36"
              ></path>
            </g>
          </svg>
          <input type="password" placeholder="••••••••••••" v-model="reNewPassword" required />
        </div>
      </div>
      <button @click="handleReset">Reset password</button>
    </form>
    <div v-if="successMessage" class="error-message success-message">
      <svg width="25" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM12 17.75C12.4142 17.75 12.75 17.4142 12.75 17V11C12.75 10.5858 12.4142 10.25 12 10.25C11.5858 10.25 11.25 10.5858 11.25 11V17C11.25 17.4142 11.5858 17.75 12 17.75ZM12 7C12.5523 7 13 7.44772 13 8C13 8.55228 12.5523 9 12 9C11.4477 9 11 8.55228 11 8C11 7.44772 11.4477 7 12 7Z"
          fill="#458588"
        ></path>
      </svg>
      <div>{{ successMessage }}</div>
    </div>
    <div v-if="errorMessage" class="error-message">
      <svg width="25" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM12 17.75C12.4142 17.75 12.75 17.4142 12.75 17V11C12.75 10.5858 12.4142 10.25 12 10.25C11.5858 10.25 11.25 10.5858 11.25 11V17C11.25 17.4142 11.5858 17.75 12 17.75ZM12 7C12.5523 7 13 7.44772 13 8C13 8.55228 12.5523 9 12 9C11.4477 9 11 8.55228 11 8C11 7.44772 11.4477 7 12 7Z"
          fill="#cc241d"
        ></path>
      </svg>
      <div>{{ errorMessage }}</div>
    </div>
  </div>
</template>

<style scoped>
.main {
  border-radius: 6px;
  background: #fffaf5;
  box-shadow: 0 0 36px rgba(40, 31, 22, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 30px;
  width: fit-content;
  height: fit-content;
  padding: 35px 30px;
  margin: 0 auto;
}
.login-logo {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
}

form {
  display: flex;
  flex-direction: column;
  row-gap: 20px;
}

.password {
  background: rgba(116, 140, 58, 0.7);
  width: 330px;
  height: fit-content;
  padding: 18px;
  border-radius: 20px;
  box-shadow: 0 0 42px rgba(143, 172, 145, 0.2);
  display: flex;
  flex-direction: column;
  row-gap: 5px;
}

.password-input {
  display: flex;
  column-gap: 5px;
}

input {
  outline: none;
  background: rgba(116, 140, 58, 0.03);
}

::placeholder {
  color: #634b36;
  opacity: 0.4;
}

.st0 {
  fill: #556358;
}

button {
  background: #748c3a;
  font-size: 18px;
  color: #ffdbb7;
  flex: center;
  width: 100%;
  border-radius: 15px;
  padding: 10px 0;
}

.error-message {
  color: #cc241d;
  display: flex;
  align-items: center;
  column-gap: 3px;
}
.success-message {
  color: #458588;
}
</style>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const email = ref('')
const isSending = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleSubmit = async () => {
  isSending.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    await axios.post('http://127.0.0.1:8000/auth/users/reset_password/', {
      email: email.value
    })
    successMessage.value = 'Letter sent successfully.'
  } catch (error) {
    errorMessage.value = error.response.data.detail || 'Error sending request.'
  } finally {
    isSending.value = false
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
    <form @submit.prevent="handleSubmit">
      <div class="email">
        <label for="email">Email address</label>
        <div class="email-input">
          <svg
            viewBox="0 0 6.3500002 6.3500002"
            id="svg1976"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:cc="http://creativecommons.org/ns#"
            xmlns:dc="http://purl.org/dc/elements/1.1/"
            xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
            xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
            xmlns:svg="http://www.w3.org/2000/svg"
            fill="#000000"
            width="21px"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <defs id="defs1970"></defs>
              <g id="layer1" style="display: inline">
                <path
                  d="m 0.87513983,0.92604163 c -0.4802584,0 -0.8748817925,0.39462207 -0.8748817925,0.87488207 v 2.7481528 c 0,0.4802611 0.3946233925,0.8748819 0.8748817925,0.8748819 H 5.4748603 c 0.4802585,0 0.8748817,-0.3946208 0.8748817,-0.8748819 V 1.8009237 c 0,-0.48026 -0.3946232,-0.87488207 -0.8748817,-0.87488207 z M 1.2549624,1.984375 a 0.264583,0.264583 0 0 1 0.1829329,0.06873 l 1.2774428,1.1539337 c 0.2490602,0.2251498 0.6728487,0.2251498 0.9219063,0 l 1.2769268,-1.153934 a 0.264583,0.264583 0 0 1 0.1839674,-0.068213 0.264583,0.264583 0 0 1 0.1912012,0.08785 0.264583,0.264583 0 0 1 -0.019632,0.3725873 l -0.7761817,0.7017658 0.1472777,0.1462455 0.6387227,0.63872 a 0.264583,0.264583 0 0 1 0,0.3746527 0.264583,0.264583 0 0 1 -0.3751713,0 L 4.266151,3.6679928 4.1007864,3.5015964 3.9922649,3.5997806 c -0.4586684,0.4146206 -1.173779,0.4146206 -1.632458,0 L 2.251804,3.5021123 2.0864394,3.6679928 1.4477167,4.3067129 a 0.264583,0.264583 0 0 1 -0.3751713,0 0.264583,0.264583 0 0 1 0,-0.3746527 L 1.7112681,3.2933402 1.8585458,3.1470947 1.0823641,2.4453289 A 0.264583,0.264583 0 0 1 1.062732,2.0727416 0.264583,0.264583 0 0 1 1.2549677,1.984375 Z"
                  id="rect868"
                  style="fill: #634b36"
                ></path>
              </g>
            </g>
          </svg>
          <input
            type="email"
            id="email"
            placeholder="Username@gmail.com"
            v-model="email"
            required
          />
        </div>
      </div>
      <button @click="handleSubmit">Send email</button>
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

.email {
  background-color: rgba(116, 140, 58, 0.7);
  width: 330px;
  height: fit-content;
  padding: 18px;
  border-radius: 20px;
  box-shadow: 0 0 42px rgba(143, 172, 145, 0.2);
  display: flex;
  flex-direction: column;
  row-gap: 5px;
}

.email-input {
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

<script setup>
import { ref } from 'vue'
import { signUp } from '../services/auth'

const username = ref('')
const email = ref('')
const password = ref('')
const re_password = ref('')

const handleSignUp = () => {
  signUp(username.value, email.value, password.value, re_password.value)
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
          fill="#CEFFD0"
        ></path>
      </svg>
      <span>SignUp</span>
    </div>
    <form @submit.prevent="signUp">
      <div class="email">
        <label for="email">Username</label>
        <div class="email-input">
          <svg
            fill="#556358"
            width="20"
            version="1.1"
            id="Layer_1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="796 796 200 200"
            enable-background="new 796 796 200 200"
            xml:space="preserve"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <g>
                <g>
                  <path
                    d="M987.675,969.676c-6.521-22.754-21.304-41.99-40.878-54.33c-3.862-2.435-8.873-2.039-12.299,0.979 c-10.504,9.251-23.506,14.76-37.618,14.76c-14.391,0-27.624-5.723-38.236-15.304c-3.388-3.058-8.374-3.519-12.269-1.14 c-20.15,12.303-35.401,31.837-42.052,55.035c-1.787,6.223-0.531,12.933,3.364,18.109c3.905,5.169,10.005,8.215,16.48,8.215 h143.661c6.48,0,12.582-3.034,16.486-8.215C988.216,982.608,989.462,975.906,987.675,969.676z"
                  ></path>
                  <path
                    d="M948.091,856.479c0,33.403-22.929,60.484-51.211,60.484c-28.28,0-51.206-27.081-51.206-60.484 c0-33.406,22.925-60.479,51.206-60.479C925.162,796,948.091,823.073,948.091,856.479z"
                  ></path>
                </g>
              </g>
            </g>
          </svg>
          <input type="text" placeholder="MobyDick" v-model="username" required />
        </div>
      </div>
      <div class="email">
        <label for="email">Email address</label>
        <div class="email-input">
          <svg
            style="padding-top: 2px"
            height="21px"
            width="21px"
            version="1.1"
            id="_x32_"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 512 512"
            xml:space="preserve"
            fill="#000000"
          >
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
            <g id="SVGRepo_iconCarrier">
              <g>
                <path
                  class="st0"
                  d="M440.917,67.925H71.083C31.827,67.925,0,99.752,0,139.008v233.984c0,39.256,31.827,71.083,71.083,71.083 h369.834c39.255,0,71.083-31.827,71.083-71.083V139.008C512,99.752,480.172,67.925,440.917,67.925z M178.166,321.72l-99.54,84.92 c-7.021,5.992-17.576,5.159-23.567-1.869c-5.992-7.021-5.159-17.576,1.87-23.567l99.54-84.92c7.02-5.992,17.574-5.159,23.566,1.87 C186.027,305.174,185.194,315.729,178.166,321.72z M256,289.436c-13.314-0.033-26.22-4.457-36.31-13.183l0.008,0.008l-0.032-0.024 c0.008,0.008,0.017,0.008,0.024,0.016L66.962,143.694c-6.98-6.058-7.723-16.612-1.674-23.583c6.057-6.98,16.612-7.723,23.582-1.674 l152.771,132.592c3.265,2.906,8.645,5.004,14.359,4.971c5.706,0.017,10.995-2.024,14.44-5.028l0.074-0.065l152.615-132.469 c6.971-6.049,17.526-5.306,23.583,1.674c6.048,6.97,5.306,17.525-1.674,23.583l-152.77,132.599 C282.211,284.929,269.322,289.419,256,289.436z M456.948,404.771c-5.992,7.028-16.547,7.861-23.566,1.869l-99.54-84.92 c-7.028-5.992-7.861-16.546-1.869-23.566c5.991-7.029,16.546-7.861,23.566-1.87l99.54,84.92 C462.107,387.195,462.94,397.75,456.948,404.771z"
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
      <div class="password">
        <label for="password">Password</label>
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
                fill="#556358"
              ></path>
            </g>
          </svg>
          <input
            type="password"
            id="password"
            placeholder="••••••••••••"
            v-model="password"
            required
          />
        </div>
      </div>
      <div class="password">
        <label for="password">Re password</label>
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
                fill="#556358"
              ></path>
            </g>
          </svg>
          <input type="password" placeholder="••••••••••••" v-model="re_password" required />
        </div>
      </div>
      <button @click="handleSignUp">SignUp</button>
    </form>
    <div class="bottom-links">
      <RouterLink to="/login" class="login-low">Log in</RouterLink>
      <RouterLink to="/" class="forgot-pass">Forgot password?</RouterLink>
    </div>
    <!--<div v-if="error" class="error-message">
      <svg width="25" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM12 17.75C12.4142 17.75 12.75 17.4142 12.75 17V11C12.75 10.5858 12.4142 10.25 12 10.25C11.5858 10.25 11.25 10.5858 11.25 11V17C11.25 17.4142 11.5858 17.75 12 17.75ZM12 7C12.5523 7 13 7.44772 13 8C13 8.55228 12.5523 9 12 9C11.4477 9 11 8.55228 11 8C11 7.44772 11.4477 7 12 7Z"
          fill="#ec6969"
        ></path>
      </svg>
      <div>{{ error }}</div>
        </div>-->
  </div>
</template>

<style scoped>
.main {
  border-radius: 6px;
  background: #fff;
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

.email,
.password {
  background: rgba(206, 255, 208, 0.7);
  width: 330px;
  height: fit-content;
  padding: 18px;
  border-radius: 20px;
  box-shadow: 0 0 42px rgba(143, 172, 145, 0.2);
  display: flex;
  flex-direction: column;
  row-gap: 5px;
}

.email-input,
.password-input {
  display: flex;
  column-gap: 5px;
}

input {
  outline: none;
  background: rgba(206, 255, 208, 0.15);
}

.st0 {
  fill: #556358;
}

button {
  background: #049548;
  font-size: 18px;
  color: #ceffd0;
  flex: center;
  width: 100%;
  border-radius: 15px;
  padding: 10px 0;
}

.bottom-links {
  display: flex;
  justify-content: space-between;
}
.bottom-links .login-low,
.bottom-links .forgot-pass {
  font-size: 14px;
  opacity: 0.7;
  cursor: pointer;
}
.bottom-links .login-low:hover,
.bottom-links .forgot-pass:hover {
  opacity: 1;
  transition: all 0.2s linear;
}

.error-message {
  color: #ec6969;
  display: flex;
  align-items: center;
  column-gap: 3px;
}
</style>

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
          fill="#748c3a"
        ></path>
      </svg>
      <span>SignUp</span>
    </div>
    <form @submit.prevent="signUp">
      <div class="email">
        <label for="email">Username</label>
        <div class="email-input">
          <svg
            fill="#634b36"
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
                fill="#634b36"
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
                fill="#634b36"
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

.email,
.password {
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

.email-input,
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
  color: #cc241d;
  display: flex;
  align-items: center;
  column-gap: 3px;
}
</style>

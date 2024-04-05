<template>
    <div>
        <input type="email" v-model="email" placeholder="Email">
        <input type="password" v-model="password" placeholder="Password">
        <button @click="login">Login</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        login() {
            axios.post('http://127.0.0.1:8000/auth/jwt/create/', {
                email: this.email,
                password: this.password
            })
            // save token
            .then(response => {
                const token = response.data.access;
                localStorage.setItem('token', token);
                console.log(token);
                console.log('successful auth');
            })
            .catch(error => {
                console.error('login error', error);
            });
        }
    }
}
</script>

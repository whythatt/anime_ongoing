<template>
    <div>
        {{ user.username }}
        <br>
        {{ user.email }}
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            user: {}
        };
    },

    methods: {
        fetchUserData() {
            const token = localStorage.getItem('token');

            if (token) {
                axios.get('http://127.0.0.1:8000/auth/users/me/', {
                    headers: {
                        'Authorization': `JWT ${token}`
                    }
                })
                .then(response => {
                    this.user = response.data;
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error.response.data);
                });
            } else {
                console.error('Токен не найден в localStorage');
            }
        }
    },
    mounted() {
        this.fetchUserData();
    }
}
</script>

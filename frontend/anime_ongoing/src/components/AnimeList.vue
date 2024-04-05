<template>
    <div>
        <h2>{{ user.id }}</h2>
        <div v-for="anime in animes" :key="anime.id">
            <div class="anime">
                <p>{{ anime.id }}</p>
                <p>{{ anime.title }}</p>
                <button @click="addToFavorites(anime.id, user.id)">Add to favorite</button>
                <br><br>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            animes: [],
            user: {}
        }
    },

    methods: {
        fetchAnimeData() {
            axios.get('http://127.0.0.1:8000/api/animes/')
            .then(response => {
                this.animes = response.data;
                console.log(response.data);
            })
            .catch(error => {
                    console.error(error.response.data);
            });
        },

        addToFavorites(animeId, userId) {
            const token = localStorage.getItem('token');

            axios.post('http://127.0.0.1:8000/api/add_favorite_anime/', 
                { anime_id: animeId, user_id: userId }, {
                headers: {
                    'Authorization': `JWT ${token}`
                },

            })
            .then(response => {
                console.log('add to favorite');
            })
        },
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
        this.fetchAnimeData();
        this.fetchUserData();
    }
}
</script>

<template>
    <div>
        <h2>{{ user.id }}</h2>
        <div v-for="anime in animes" :key="anime.id">
            <div class="anime">
                <p>{{ anime.id }}</p>
                <p>{{ anime.title }}</p>
                <button @click="addToFavorites(anime.id, user.id)">Add to favorite</button>
                <button @click="deleteFavorites(anime.id, user.id)">Delete from favorite</button>
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
        }
    },

    computed: {
        user() {
            return this.$store.state.user;
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
                console.log(error.message);
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
    },
    mounted() {
        this.fetchAnimeData();
    }
}
</script>

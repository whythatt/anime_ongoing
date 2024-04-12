<template>
    <div>
        <div v-for="anime in animes" :key="anime.id">
            <div class="anime">
                <p>{{ anime.id }}</p>
                <p>{{ anime.title }}</p>
                <button @click="addToFavorites(anime.id)">Add to favorite</button>
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
        addToFavorites(animeId) {
            const token = localStorage.getItem('token');

            axios.post('http://127.0.0.1:8000/api/add_to_favorites/', 
                { anime_id: animeId }, {
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

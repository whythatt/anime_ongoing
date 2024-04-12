<template>
    <div>
        <h1 style="margin: 0 auto 0 auto;">FavoritesList</h1>
        {{ user }}
        <div v-for="favorite in favorites_list" :key="favorite.id">
            <div class="favorite">
                <p>User: {{ favorite.user }} | Anime {{  favorite.anime }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            favorites_list: [],
        }
    },
    methods: {
        fetchFavoritesList() {
            const token = localStorage.getItem('token');

            axios.get('http://127.0.0.1:8000/api/favorites_list/', {
                headers: {
                    'Authorization': `JWT ${token}`
                },
            })
            .then(response => {
                this.favorites_list = response.data;
                console.log(response.data);
            })
            .catch(error => {
                console.log(error.message);
            })
        },
    },
    mounted() {
        this.fetchFavoritesList();
    }
}
</script>

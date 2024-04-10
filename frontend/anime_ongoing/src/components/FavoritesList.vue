<template>
    <div>
        <h1 style="margin-left: auto; margin-right: auto;">FavoritesList</h1>
        <div v-for="favorite in favorites_list" :key="favorite.id">
            <div class="favorite">
                <p>{{ favorite.user }}</p>
                <p>{{ favorite.anime }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            favorites_list: []
        }
    },

    methods: {
        fetchFavoritesList() {
            const token = localStorage.getItem('token');

            axios.get('http://127.0.0.1:8000/api/favorites_list/', {
                headers: {
                    'Authorization': `JWT {token}`
                },
            })
            .then(response => {
                this.favorites_list = response.data;
                console.log(response.data);
            })
            .catch(error => {
                console.error(error.response.data);
            })
        }
    },
}
</script>

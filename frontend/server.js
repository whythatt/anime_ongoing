const express = require('express');
const fetch = require('node-fetch');
const axios = require('axios');
const app = express();
const port = 3000;


app.get('/favoriteAnime', async (req, res) => {
    try {
        const apiUrl = 'http://127.0.0.1:8000/api/favorite_anime/';
        const response = await axios.get(apiUrl);
        const data = response.data;
        res.json(data);
    } catch (error) {
        console.error('Ошибка получения данных из API:', error);
        res.status(500).send('Произошла ошибка при получении данных');
    }
});

app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});

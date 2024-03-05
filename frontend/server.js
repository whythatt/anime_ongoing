const express = require('express');
const fetch = require('node-fetch');
const app = express();
const port = 3000;

// Маршрут для получения данных с API аниме
app.get('/api/animes/', async (req, res) => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/animes/');
        const data = await response.json();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Ошибка при получении данных с API аниме' });
    }
});

// Маршрут для получения данных с API избранных аниме
app.get('/api/favorite/', async (req, res) => {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/favorite/');
        const data = await response.json();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Ошибка при получении данных с API favorite аниме' });
    }
});

// Статический файл для клиентской стороны
app.use(express.static('public'));

// Слушаем на порту 3000
app.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});

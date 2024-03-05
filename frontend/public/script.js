fetch('/api/animes')
    .then(response => response.json())
    .then(animeData => {
        const animeList = document.getElementById('anime-list');
        animeData.forEach(anime => {
            const listItem = document.createElement('li');
            listItem.textContent = anime.title; // Предположим, что данные содержат поле 'title'
            animeList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Ошибка при получении данных с API аниме:', error));

fetch('/api/favorite')
    .then(response => response.json())
    .then(favoriteData => {
        const favoriteAnimeList = document.getElementById('favorite-anime-list');
        favoriteData.forEach(favoriteAnime => {
            const listItem = document.createElement('li');
            listItem.textContent = favoriteAnime.anime.title; // Предположим, что данные содержат поле 'title'
            favoriteAnimeList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Ошибка при получении данных с API избранных аниме:', error));

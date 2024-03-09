// fetch('/api/animes')
//     .then(response => response.json())
//     .then(animeData => {
//         const animeList = document.getElementById('anime-list');
//         animeData.forEach(anime => {
//             const listItem = document.createElement('li');
//             listItem.textContent = anime.title; // Предположим, что данные содержат поле 'title'
//             animeList.appendChild(listItem);
//         });
//     })
//     .catch(error => console.error('Ошибка при получении данных с API аниме:', error));

fetch('http://127.0.0.1:8000/api/favorite_anime/')
    .then(response => response.json())
    .then(favoriteData => {
        const favoriteAnimeList = document.getElementById('main');
        favoriteData.forEach(favoriteAnime => {
            const animeItem = document.createElement('div');
            animeItem.id = 'main_anime';


            animeItem.innerHTML = `
                <div class="image"></div>
                <div class="bg_info">
                    <div class="block_with_info">
                        <span class="title">${favoriteAnime.anime.title}</span>
                        <div class="info_with_icons">
                            <div class="score">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                     width="11"
                                     height="11"
                                     fill="currentColor"
                                     class="bi bi-star-fill"
                                     viewBox="0 0 16 16">
                                    <path d="M3.612 15.443c-.386.198-.824-.149-.746-.592l.83-4.73L.173 6.765c-.329-.314-.158-.888.283-.95l4.898-.696L7.538.792c.197-.39.73-.39.927 0l2.184 4.327 4.898.696c.441.062.612.636.282.95l-3.522 3.356.83 4.73c.078.443-.36.79-.746.592L8 13.187l-4.389 2.256z" />
                                </svg>
                                <span id="score">${favoriteAnime.anime.score}</span>
                            </div>
                            <div class="mediatype">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                     width="15"
                                     height="15"
                                     fill="currentColor"
                                     class="bi bi-caret-right-fill"
                                     viewBox="0 0 16 16">
                                    <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z" />
                                </svg>
                                <span id="mediatype">${favoriteAnime.anime.mediatype}</span>
                            </div>
                            <div class="duration">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                     width="10"
                                     height="10"
                                     fill="currentColor"
                                     class="bi bi-clock-fill"
                                     viewBox="0 0 16 16">
                                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71z" />
                                </svg>
                                <span id="duration">${favoriteAnime.anime.episode_duration}</span>
                            </div>
                            <div class="release_date_next_ep">
                                <svg xmlns="http://www.w3.org/2000/svg"
                                     width="10"
                                     height="10"
                                     fill="currentColor"
                                     class="bi bi-calendar-fill"
                                     viewBox="0 0 16 16">
                                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V5h16V4H0V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5" />
                                </svg>
                                <span id="release_date_next_ep">${favoriteAnime.anime.release_date_next_ep}</span>
                            </div>
                        </div>
                        <div class="info_without_icons">
                            <div class="status">
                                Status: <span id="status">${favoriteAnime.anime.status}</span>
                            </div>
                            <div class="number_episodes">
                                Number of episodes: <span id="number_episodes">${favoriteAnime.anime.total_episodes}</span>
                            </div>
                            <div class="release_date">
                                Release date: <span id="release_date">${favoriteAnime.anime.release_date}</span>
                            </div>
                        </div>
                        <p class="description">${favoriteAnime.anime.description}</p>
                        <div class="button">
                            <button class="remove_btn">Remove</button>
                        </div>
                    </div>
                </div>
            `;
            favoriteAnimeList.appendChild(animeItem);
        });
    })
    .catch(error => console.error('Ошибка при получении данных с API избранных аниме:', error));

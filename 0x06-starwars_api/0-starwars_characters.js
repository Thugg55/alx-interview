#!/usr/bin/node
// STAR WARS API

const axios = require('axios');

async function getMovieCharacters(movieId) {
    try {
        // Fetch the movie details from the Star Wars API
        const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
        const characters = response.data.characters;

        // Fetch and print each character's name
        for (const characterUrl of characters) {
            const characterResponse = await axios.get(characterUrl);
            console.log(characterResponse.data.name);
        }
    } catch (error) {
        console.error('An error occurred:', error.message);
    }
}

const movieId = process.argv[2];

if (!movieId) {
    console.error("Usage: node script.js <movie_id>");
    process.exit(1);
}

getMovieCharacters(movieId);


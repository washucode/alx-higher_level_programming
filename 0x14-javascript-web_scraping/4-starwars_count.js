#!/usr/bin/node
/*
    * Script that prints the number of movies where the character “Wedge Antilles” is present.
    * The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
    * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
    * You must use the module request
*/

const request = require('request');
const url = process.argv[2];
const characterId = '18';

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    for (const film of films) {
      for (const char of film.characters) {
        if (char.endsWith('/' + characterId + '/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

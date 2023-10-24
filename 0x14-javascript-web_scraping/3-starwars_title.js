#!/usr/bin/node
/*
  * Script that prints the title of a Star Wars movie where the episode number matches a given integer.
  * The first argument is the movie ID.
  * You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
  * You must use the module request.
*/

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});

#!/usr/bin/node
/*
    * Script that prints all characters of a Star Wars movie:
    * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
    * Display one character name by line in the same order of the list “characters” in the /films/ response
    * You must use the Star wars API
    * You must use the module request
*/

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Function to get the name of a character
function getName (character) {
  return new Promise((resolve, reject) => {
    request(character, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

// Function to get the names of all characters in a list
async function getNames (characters) {
  const names = [];
  for (const character of characters) {
    names.push(await getName(character));
  }
  return names;
}

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    const names = await getNames(characters);
    for (const name of names) {
      console.log(name);
    }
  }
});

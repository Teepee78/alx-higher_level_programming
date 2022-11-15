#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
const request = require('request');

const url = process.argv[2];
const characterUrl = 'https://swapi-api.hbtn.io/api/people/18/';
let movies = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    let results = JSON.parse(body).results;
    results.forEach(element => {
      element.characters.forEach(character => {
        // check for character
        if (character === characterUrl) {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});

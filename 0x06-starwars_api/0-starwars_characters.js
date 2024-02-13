#!/usr/bin/node
// script  that prints all characters of a Star Wars movie
const request = require('request');
const argument = process.argv[2];
const urlFilms = `https://swapi-api.alx-tools.com/api/films/${argument}`;

function toRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, resp, body) {
      if (!err && resp.statusCode === 200) {
        resolve(body);
      } else {
        reject(err);
      }
    });
  });
}

async function getCharacterName () {
  // making the first request and waiting the response
  const bodyResp = await toRequest(urlFilms);
  // parsing the string to object using Json
  const film = JSON.parse(bodyResp);
  // extraction all the charactersUrl (array)
  const charactersUrl = film.characters;

  // map each character Url to a promise
  // charactersPromises is an array of promises
  const charactersPromises = charactersUrl.map(cUrl => toRequest(cUrl));

  // waiting all the promises to be resolved
  // Promise.all() execute the promises in a prallel way
  // then return a single Promise that resolves with an array
  // of the results of the input promises,
  // in the same order as the input.
  const charactersObjStr = await Promise.all(charactersPromises);

  const charactersNames = charactersObjStr.map(c => {
    const character = JSON.parse(c);
    return character.name;
  });

  charactersNames.forEach(name => console.log(name));
}

getCharacterName();

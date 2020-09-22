#!/usr/bin/node
/* script that prints the title of a Star Wars */

const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});

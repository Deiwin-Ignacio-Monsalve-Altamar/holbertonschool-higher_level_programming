#!/usr/bin/node

if (process.argv[2] !== undefined) {
  const request = require('request');
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.log(error);
    } else if (response.statusCode === 200) {
      const result = JSON.parse(body).results;
      let count = 0;
      for (let index = 0; index < result.length; index++) {
        const character = result[index].characters;
        for (let i = 0; i < character.length; i++) {
          if (character[i].includes('18')) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}

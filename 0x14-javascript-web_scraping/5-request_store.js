#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file. */
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const contents = body;
    const fs = require('fs');
    fs.writeFile(process.argv[3], contents, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});

#!/usr/bin/node
/* script that computes the number of tasks completed by user id */
const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const array = JSON.parse(body);
    const obj = {};
    for (let index = 0; index < array.length; index++) {
      if (array[index].completed) {
        if (!(array[index].userId in obj)) {
          obj[array[index].userId] = 0;
        }
        obj[array[index].userId] += 1;
      }
    }
    console.log(obj);
  }
});

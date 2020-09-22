#!/usr/bin/node
/* script that writes a string to a file. */

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});

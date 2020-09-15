#!/usr/bin/node

const len = process.argv;
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < len[2]; index++) {
    console.log('C is fun');
  }
}

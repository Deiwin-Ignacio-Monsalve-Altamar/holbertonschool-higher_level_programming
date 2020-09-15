#!/usr/bin/node

const number = process.argv[2];
const parseo = parseInt(number, 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseo}`);
}

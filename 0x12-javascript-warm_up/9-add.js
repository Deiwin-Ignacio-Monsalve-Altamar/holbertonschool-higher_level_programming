#!/usr/bin/node

const fisrtNumber = process.argv[2];
const secondNumber = process.argv[3];
if (isNaN(fisrtNumber) || isNaN(fisrtNumber)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(fisrtNumber), parseInt(secondNumber)));
}

function add (a, b) {
  return a + b;
}

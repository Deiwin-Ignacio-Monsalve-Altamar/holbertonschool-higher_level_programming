#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined) {
  console.log('1');
} else {
  const result = factorial(parseInt(args[2]));
  console.log(result);
}

function factorial (num) {
  if (num === 1) {
    return num;
  }
  return num * factorial(num - 1);
}

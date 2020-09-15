#!/usr/bin/node

if (process.argv[2] === undefined | isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let index = 1; index <= process.argv[2]; index++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

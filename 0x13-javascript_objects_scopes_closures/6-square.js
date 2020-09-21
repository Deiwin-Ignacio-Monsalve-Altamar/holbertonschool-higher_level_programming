#!/usr/bin/node
/* Square that defines a square and inherits from Square of 5-square.js */

const Rectangulo = require('./5-square');
class Square extends Rectangulo {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

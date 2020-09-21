#!/usr/bin/node
/* that returns the number of occurrences in a list: */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      count++;
    }
  }
  return count;
};

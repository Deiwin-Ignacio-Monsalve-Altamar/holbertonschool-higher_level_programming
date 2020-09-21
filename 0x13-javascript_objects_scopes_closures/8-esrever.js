#!/usr/bin/node
/* that returns the reversed version of a list */

exports.esrever = function (list) {
  const listReverse = [];
  while (list.length) {
    listReverse.push(list.pop());
  }
  return listReverse;
};

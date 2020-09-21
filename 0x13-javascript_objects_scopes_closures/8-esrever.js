#!/usr/bin/node
/* that returns the reversed version of a list */

exports.esrever = function (list) {
  const list_reverse = [];
  while (list.length) {
    list_reverse.push(list.pop());
  }
  return list_reverse;
};

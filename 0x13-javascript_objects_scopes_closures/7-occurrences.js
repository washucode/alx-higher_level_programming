#!/usr/bin/node
// Script that returns the number of occurrences in a list.

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const e of list) {
    if (e === searchElement) {
      counter++;
    }
  }
  return counter;
};

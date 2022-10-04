#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  for (const element of list) {
    if (element === searchElement) {
      occur++;
    }
  }

  return occur;
};

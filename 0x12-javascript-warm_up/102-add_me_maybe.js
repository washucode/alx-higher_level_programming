#!/usr/bin/node
// Script that modifies the value of myVar to 333

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};

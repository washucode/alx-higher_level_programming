#!/usr/bin/node
// Script that prints the addition of 2 integers

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('NaN');
} else {
  console.log(parseInt(args[0]) + parseInt(args[1]));
}

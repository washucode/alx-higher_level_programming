#!/usr/bin/node
// Script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
// If the argument can’t be converted to an integer, print “Not a number”

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Not a number');
} else if (isNaN(args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0]));
}

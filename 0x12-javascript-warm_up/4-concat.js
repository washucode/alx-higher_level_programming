#!/usr/bin/node
// Script that prints two arguments passed to it, in the following format: “ is ”

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('undefined is undefined');
} else if (args.length === 1) {
  console.log(args[0] + ' is undefined');
} else {
  console.log(args[0] + ' is ' + args[1]);
}

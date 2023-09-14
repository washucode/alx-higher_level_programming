#!/usr/bin/node
// Script that prints x times “C is fun”

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(args[0]); i++) {
    console.log('C is fun');
  }
}

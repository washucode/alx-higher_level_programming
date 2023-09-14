#!/usr/bin/node
// Script that prints a square

const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Missing size');
} else if (isNaN(args[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[0]); i++) {
    console.log('X'.repeat(parseInt(args[0])));
  }
}

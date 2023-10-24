#!/usr/bin/node
/*
    * Script that reads and prints the content of a file.
    * The first argument is the file path.
    * The content of the file must be read in utf-8.
    * If an error occurred during the reading, print the error object.
    * You must use the module fs.
    * You must use the function readFileSync from the fs module.
    * You are not allowed to use console.log(...).
    * You must use console.error to print the error objects.
*/

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    process.stdout.write(data);
  }
});

#!/usr/bin/node
/*
    * Script that computes the number of tasks completed by user id.
    * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
    * You must use the module request.
 */

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const allTasks = JSON.parse(body);
    const completedTasks = {};
    for (const task of allTasks) {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});

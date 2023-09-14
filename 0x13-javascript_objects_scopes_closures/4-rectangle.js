#!/usr/bin/node
// Script that prints the rectangle with X

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;

      this.print = function () {
        for (let i = 0; i < this.height; i++) {
          console.log('X'.repeat(this.width));
        }
      };
      this.rotate = function () {
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
      };
      this.double = function () {
        this.width *= 2;
        this.height *= 2;
      };
    }
  }
}
module.exports = Rectangle;

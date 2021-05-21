"use strict";
const main = input => {
  input = input.split('');
  const squares = input.map(elem => (
    elem !== '\n' ? parseInt(elem) : null
  ))
  const sum = squares.reduce((sum, val) => (
    sum + val
  ));
  console.log(sum);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
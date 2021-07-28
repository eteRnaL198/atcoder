"use strict";
const main = input => {
  input = input.trim().split("\n");
  input[1] = input[1].split(" ").map((num) => parseInt(num));
  const n = parseInt(input[0]);
  
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
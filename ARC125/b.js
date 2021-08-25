"use strict";
const main = input => {
  input = input.trim().split(" ").map(c => parseInt(c));
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
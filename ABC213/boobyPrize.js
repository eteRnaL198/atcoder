"use strict";
const main = input => {
  input = input.trim().split("\n");
  const scores = input[1].split(" ").map(c => parseInt(c));
  const map = {};
  scores.forEach((score, idx) => {
    map[score] = idx+1;
  })
  scores.sort((a, b) => b - a);
  console.log(map[scores[1]]);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
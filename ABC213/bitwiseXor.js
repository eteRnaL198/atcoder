"use strict";
const main = input => {
  const [a, b] = input.trim().split(" ").map(c => parseInt(c));
  const c = a^b;
  console.log(c);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
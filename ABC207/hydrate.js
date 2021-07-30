"use strict";
const main = input => {
  const [a, b, c, d] = input.trim().split(" ").map(c => parseInt(c));
  const min = c*d <= b ? -1 : Math.ceil(a/(c*d - b));
  console.log(min);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
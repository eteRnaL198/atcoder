"use strict";
const main = input => {
  const [a, b] = input.trim().split(" ");
  const cal = a * b / 100;
  console.log(cal);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
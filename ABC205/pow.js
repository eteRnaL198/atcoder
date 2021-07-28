"use strict";
const main = input => {
  const [a, b, c] = input.trim().split(" ").map((num) => parseInt(num));
  let sign = "=";
  if(c % 2 === 0) {
    sign = Math.abs(a) < Math.abs(b) ? "<" : sign;
    sign = Math.abs(a) > Math.abs(b) ? ">" : sign;
  } else {
    sign = a < b ? "<" : sign;
    sign = a > b ? ">" : sign;
  }
  console.log(sign);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
"use strict";
const main = input => {
  const n = input.trim().split(" ").map(c => parseInt(c));
  let num;
  if(n <= 125) {
    num = 4;
  } else if(n <= 211) {
    num = 6;
  } else if(n <= 214) {
    num = 8;
  }
  console.log(num);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
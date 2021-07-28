"use strict";
const main = input => {
  const n = input.trim().split("\n").map((num) => parseInt(num));
  let i=1;
  while(n > i*(i+1)/2) i++;
  console.log(i);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
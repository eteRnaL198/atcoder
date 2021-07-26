"use strict";
const main = input => {
  input = input.trim().split(' ');
  const n = parseInt(input[0]);
  const k = parseInt(input[1]);
  let sum = 0;
  for(let i=1; i<=n; i++) {
    for(let j=1; j<=k; j++) {
      sum += i*100 + j;
    }
  }
  console.log(sum);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
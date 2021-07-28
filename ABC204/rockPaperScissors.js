"use strict";
const main = input => {
  input = input.trim().split(" ");
  const x = parseInt(input[0]);
  const y = parseInt(input[1]);
  let z;
  if(x == y) z = x;
  else z = 3 - (x + y);
  console.log(z);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
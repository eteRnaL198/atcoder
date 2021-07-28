"use strict";
const main = input => {
  input = input.trim().split("\n");
  const n = input[0];
  const a = input[1].split(" ").map(num => parseInt(num));
  a.sort((a, b) => a - b);
  let flag = true;
  a.forEach((num, idx) => {
    if(num !== idx+1) flag = false;
  })
  const result = flag ? "Yes" : "No";
  console.log(result);

}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
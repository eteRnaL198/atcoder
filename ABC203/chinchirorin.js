"use strict";
const main = input => {
  const nums = input.trim().split(' ');
  let remainingNum = 0;
  nums.forEach((num, idx) => {
    if(num === nums[(idx+1)%3]) {
      remainingNum = nums[(idx+2)%3];
    }
  });
  console.log(remainingNum);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
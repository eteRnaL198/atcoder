"use strict";
const main = input => {
  const nums = input.trim().split(" ").map((num) => parseInt(num));
  nums.sort((a, b) => b - a);
  const sum = nums[0] + nums[1];
  console.log(sum);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
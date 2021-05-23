"use strict"
const main = input => {
  input = input.split('\n');
  input.shift();
  input.pop();
  const nums = input.filter((num, idx, nums) => (
    nums.lastIndexOf(num) === idx
  ));
  console.log(nums.length);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
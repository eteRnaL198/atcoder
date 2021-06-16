"use strict";
const main = input => {
  input = input.split('\n');
  input.pop();
  const nums = input[0].split('');
  const numsArr = nums.map(num => parseInt(num, 10));
  const reversed = numsArr.map((val, idx, nums) => (
    nums[nums.length - idx - 1]
  ));
  const rotated = reversed.map(val => {
    switch(val) {
      case 6:
        return 9;
      case 9:
        return 6;
      default:
        return val;
    }
  });
  console.log(rotated.join(''));
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
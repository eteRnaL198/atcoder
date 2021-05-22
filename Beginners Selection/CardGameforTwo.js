"use strict";
const main = input => {
  input = input.split('\n');
  const nums = input[1].split('').map(num => parseInt(num));
  const sortedNums = nums.map((elem, idx, nums) => {
    if(idx ===0) {
      for(let j=nums.length-1; j>0; j--) {
        if(nums[j-1] < nums[j]) nums.splice(j, 2, nums[j], nums[j-1]);
      }
    }
    return elem;
  });
  console.log(sortedNums);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
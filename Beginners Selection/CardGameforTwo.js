"use strict";
const main = input => {
  input = input.split('\n');
  const nums = input[1].split(' ').map(num => parseInt(num));
  const sortedNums = nums.map((elem, idx, nums) => {
    for(let j=nums.length-1; j>idx; j--) {
      if(nums[j-1] < nums[j]) nums.splice(j-1, 2, nums[j], nums[j-1]);
    }
    return nums[idx];
  });
  const winner = sortedNums.reduce((acc, cur, idx) => (
    (idx % 2 === 0) ? acc + cur : acc
  ), 0);
  const loser = sortedNums.reduce((acc, cur, idx) => (
    (idx % 2 !== 0) ? acc + cur : acc
  ), 0)
  console.log(winner - loser);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
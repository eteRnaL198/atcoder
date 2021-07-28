"use strict";
const main = input => {
  input = input.trim().split("\n");
  input[1] = input[1].split(" ").map((num) => parseInt(num));
  const n = parseInt(input[0]);
  const nums = input[1].sort((a, b) => a - b);
  const sames = [];
  for(let i=0; i<n-1; i++) {
    let j = 1;
    while(nums[i] === nums[i+1]) {
      j++;
      i++;
    };
    if(j !== 1) sames.push(j);
  }

  const fact = num => (
    (num <= 1) ? 1 : num * fact(num-1)
  )
  const comb = n => {
    const r = 2;
    return fact(n) / (fact(r) * fact(n-r));
  }

  const sub = sames.reduce((acc, num) => {
    return acc + comb(num);
  }, 0);
  
  const ans = (n * (n-1) / 2) - sub;
  console.log(ans);

}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
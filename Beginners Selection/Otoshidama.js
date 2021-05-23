"use strict";
const main = input => {
  input = input.split(' ');
  const n = parseInt(input[0]);
  const y = parseInt(input[1]);
  let [a, b, c] = [-1, -1, -1];
  for(let i=n; i>=0; i--) {
    const remaining_10000 = y - 10000*i;
    if(remaining_10000 < 0) continue;
    for(let j=n-i; j>=0; j--) {
      const remaining_5000 = remaining_10000 - 5000*j;
      if(remaining_5000 < 0) continue;
      if(remaining_5000 / 1000 === n-i-j) [a, b, c] = [i, j, n-i-j];
    }
  }
  console.log(a, b, c);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
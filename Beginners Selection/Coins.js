"use strict";
const main = input => {
  const [a, b, c, x] = input.split('\n');
  let combination = 0;
  for(let i=a; i>=0; i--) {
    const remaining_500 = x - 500*i;
    if(remaining_500 < 0) continue;
    for(let j=b; j>=0; j--) {
      const remaining_100 = remaining_500 - 100*j;
      if(remaining_100 < 0) continue;
      if(remaining_100/50 <= c) combination++;
    }
  }
  console.log(combination);
}
main(require("fs").readFileSync("/dev/stdin","utf8"));
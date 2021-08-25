"use strict";
const main = input => {
  const [s, t] = input.trim().split(" ").map(c => parseInt(c))
  let cnt = 0
  for(let a=0; a<=s; a++) {
    for(let b=0; b<=s; b++) {
      for(let c=0; c<=s; c++) {
        cnt += (a+b+c <= s && a*b*c <= t) ? 1 : 0
      }
    }
  }
  console.log(cnt);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
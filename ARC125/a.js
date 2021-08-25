"use strict";
const main = input => {
  input = input.trim().split("\n");
  const a = input[1].split("").map(c => parseInt(c));
  const t = input[2].split("").map(c => parseInt(c));
  let ans = 0;
  const uniqueA = [...new Set(a)];
  const uniqueT = [...new Set(t)];
  if(uniqueA.length === 1 && !uniqueT.includes(uniqueA[0])) {
    ans = -1;
    console.log(ans);
  } else {
    t.forEach((t, i) => {
      
    })
  }
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
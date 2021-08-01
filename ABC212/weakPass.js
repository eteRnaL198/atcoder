"use strict";
const main = input => {
  const pass = input.trim().split("").map(c => parseInt(c));
  let isWeak = false;

  let isOneType = true;
  for(let i=0; i<pass.length-1; i++) {
    isOneType = pass[i] !== pass[i+1] ? false : isOneType;
  }
  isWeak = isOneType ? true : isWeak;

  if(!isWeak) {
    let isStairs = true;
    for(let i=0; i<pass.length-1; i++) {
      isStairs = (pass[i] + 1) % 10 !== pass[i+1] ? false : isStairs;
    }
    isWeak = isStairs ? true : isWeak;
  }

  if(isWeak) console.log("Weak");
  else console.log("Strong");
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
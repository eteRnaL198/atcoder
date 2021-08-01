"use strict";
const main = input => {
  const lines = input.trim().split("\n");
  const tempA = lines[1].split(" ").map(c => parseInt(c, 10));
  const tempB = lines[2].split(" ").map(c => parseInt(c, 10));
  tempA.sort((a, b) => a - b);
  tempB.sort((a, b) => a - b);
  const a = Array.from(new Set(tempA));
  const b = Array.from(new Set(tempB));
  const min = a.reduce((m, aNum) => {
    let tempMin;
    for(let i=0; i<b.length; i++) {
      if(i === 0) tempMin = Math.abs(aNum - b[i]);
      else if(Math.abs(aNum - b[i]) < tempMin) tempMin = Math.abs(aNum - b[i]);
      else break;
    }
    return tempMin < m ? tempMin : m;
  }, Math.abs(a[0] - b[0]));
  console.log(min);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
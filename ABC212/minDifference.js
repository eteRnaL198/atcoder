"use strict";
const main = input => {
  const lines = input.trim().split("\n");
  const a = lines[1].split(" ").map(c => parseInt(c, 10));
  const b = lines[2].split(" ").map(c => parseInt(c, 10));
  a.sort((a, b) => a - b);
  b.sort((a, b) => a - b);
  let min = 1001001001;
  let ai = 0, bi = 0;
  while(ai < a.length && bi < b.length) {
    min = Math.abs(a[ai] - b[bi]) < min ? Math.abs(a[ai] - b[bi]) : min;
    if(a[ai] < b[bi]) ai++;
    else bi++;
  }

  console.log(min);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
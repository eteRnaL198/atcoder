"use strict";
const main = input => {
  const lines = input.trim().split("\n");
  const n = lines.shift();
  const ranges = lines.map(line => (
    line.split(" ").map(c => parseInt(c, 10))
  ))
  ranges.sort((a, b) => a[1] - b[1]);
  let count = 0;
  for(let i=0; i<n-1; i++) {
    for(let j=i+1; j<n; j++) {
      const width = ranges[i][2] - ranges[i][1];
      if(ranges[j][1] - ranges[i][1] < width) count++;
      else if(ranges[j][1] - ranges[i][1] === width) {
        if(ranges[i][0] % 2 !== 0 && ranges[j][0] - 2 <= 0) count ++;
      }
    }
  }
  console.log(count);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
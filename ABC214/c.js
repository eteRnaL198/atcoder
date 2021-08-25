"use strict";
const main = input => {
  input = input.trim().split("\n")
  const n = input[0]
  const s = input[1].split(" ").map(c => parseInt(c))
  const t = input[2].split(" ").map((c,i) => [i, parseInt(c)])
  const rec = {}
  for(let i=0; i<n; i++) {
    rec[i] = t[i][1]
  }
  t.sort((a,b) => a[1] - b[1])

  const mod = (i, j) => {
    return (i % j) < 0 ? (i % j) + 0 + (j < 0 ? -j : j) : (i % j + 0);
  }

  rec[t[0][0]] = t[0][1]
  for(let i=t[0][0]+1; i%n !== t[0][0]; i++) {
    rec[i%n] = rec[mod(i-1, n)] + s[mod(i-1, n)] < rec[i%n] ? rec[mod(i-1, n)] + s[mod(i-1, n)] : rec[i%n]
  }

  for(let i=0; i<n; i++) {
    console.log(rec[i]);
  }

}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
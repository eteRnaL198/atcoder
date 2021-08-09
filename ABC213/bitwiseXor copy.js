"use strict";
const main = input => {
  input = input.trim().split(" ").map(c => parseInt(c));
  const [a, b] = input.map(d => String(d.toString(2)));
  const ra = a.split("").reverse().join("");
  const rb = b.split("").reverse().join("");
  const c = [];
  
  const len = a.length > b.length ? a.length : b.length;
  for(let i=0; i<len; i++) {
    const num = ra[i] === rb[i] ? "0" : "1";
    c.push(num);
  }
  console.log(parseInt(c.join(""), 2));
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
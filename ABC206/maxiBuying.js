"use strict";
const main = input => {
  const n = input.trim().split("\n").map((num) => parseInt(num));
  const price = 206;
  let flag = "so-so";
  flag = Math.floor(n*1.08) < price ? "Yay!" : flag;
  flag = Math.floor(n*1.08) > price ? ":(" : flag;
  console.log(flag);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
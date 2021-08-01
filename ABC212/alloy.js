"use strict";
const main = input => {
  const [a, b] = input.trim().split(" ").map(c => parseInt(c));
  let result = "";
  if (0 < a && b === 0) {
    result = "Gold";
  } else if (a === 0 && 0 < b) {
    result = "Silver";
  } else if(0 < a && 0 < b) {
    result = "Alloy";
  }
  console.log(result);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
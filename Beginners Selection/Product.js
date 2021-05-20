"use strict";

const main = input => {
  const [a,b] = input.split(" ");
  if(a % 2 !== 0 && b % 2 !== 0) {
    console.log("Odd");
  } else {
    console.log("Even");
  }
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
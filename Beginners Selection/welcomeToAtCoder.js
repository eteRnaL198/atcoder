"use strict";

const main = input => {
  input = input.split("\n");
  const tmp = input[1].split(" ");

  const a = parseInt(input[0], 10);
  const b = parseInt(tmp[0], 10);
  const c = parseInt(tmp[1], 10);
  const s = input[2];
  console.log(a+b+c, s);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
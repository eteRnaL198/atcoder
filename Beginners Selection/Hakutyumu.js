"use strict";
const main = input => {
  input = input.split('\n');
  const s = input[0];
  // const words = ['eraser', 'erase', 'dreamer', 'dream'];
  // const remaining = words.reduce((acc, word) => {
  //   const regex = new RegExp(word,"g");
  //   return acc.replace(regex,'!');
  // }, s);
  const result = s.replace(/(eraser|erase|dreamer|dream)*/, '');
  // const result = remaining.replace('!', '');
  // console.log(result);
  const flag = (result.length === 0) ? "YES" : "NO";
  console.log(flag);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
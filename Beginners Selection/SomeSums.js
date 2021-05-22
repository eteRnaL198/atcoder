"use strict";
const main = input => {
  input = input.split(' ');
  const [n, a, b] = input.map((elem) => parseInt(elem));
  let sum = 0;
  for(let num=1; num<=n; num++) {
    const digit_num = [10000, 1000, 100, 10, 1].map((elem, idx, arr) => {
      if(idx === 0) {
        return Math.floor(num / elem);
      } else {
        return Math.floor((num % arr[idx-1]) / elem);
      }
    })
    const digit_sum = digit_num.reduce((sum, elem) => (
      sum += elem
    ))
    if(digit_sum >= a && digit_sum <= b) sum += num;
  }
  console.log(sum);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
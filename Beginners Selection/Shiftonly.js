"use strict";
const main = input => {
  input = input.split('\n');
  const ints = input[1].split(' ').map((elem) => parseInt(elem));
  const halve = (nums) => {
    return nums.map(num => {
      if(num % 2 == 0) return num / 2;
      else return -1;
    })
  }
  const result = (() => {
    let count = 0;
    let newInts = ints;
    while(true) {
      newInts = halve(newInts);
      if(newInts.includes(-1)) {
        return count;
      } else {
        count++;
      }
    }
  })();
  console.log(result);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
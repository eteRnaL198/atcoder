"use strict";
const main = input => {
  input = input.split('\n');
  input.shift();
  input.pop();
  const plans = input.map(elem => {
    const string = elem.split(' ');
    const nums = string.map(num => parseInt(num));
    return [...nums];
  });
  let flag = 0;
  let start = [0, 0, 0];
  for(let i=0; i<plans.length; i++) {
    const dif = plans[i].map((val, idx) => (Math.abs(val - start[idx])));
    if(dif[1] + dif[2] > dif[0]) {
      flag++;
      break;
    }
    else if((dif[0] - (dif[1] + dif[2])) % 2 !== 0) {
      flag++;
      break;
    }
    start = [...plans[i]];
  };
  const dec = (flag === 0) ? "Yes" : "No";
  console.log(dec);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
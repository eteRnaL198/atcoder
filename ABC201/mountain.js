"use strict";
const main = input => {
  const lines = input.trim().split('\n');
  lines.shift();
  const mountains = lines.map((val) => {
    val = val.split(' ');
    const mountain = {
      name: val[0],
      height: parseInt(val[1]),
    }
    return mountain;
  })
  const topMountains = mountains.reduce((acc, val, idx) => {
    const arr = [...acc];
    if(arr.length === 0) arr.push(idx);
    else if(val.height > mountains[acc[0]].height) {
      arr.splice(1,1,arr[0]);
      arr.splice(0,1,idx);
    }
    else if(arr.length === 1 || val.height > mountains[acc[1]].height) arr.splice(1,1,idx);
    return arr;
    }, []);
  console.log(mountains[topMountains[1]].name);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
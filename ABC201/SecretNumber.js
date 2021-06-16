"use strict";
const main = input => {
  const words = input.trim().split('');
  const certainNum = words.filter(word => word === 'o');
  const likelyNum = words.filter(word => word === '?');

  if(certainNum.length === 4) {
    const combination = 4**4;
    console.log(combination);
  } else if(certainNum.length === 3) {
    const combination = certainNum.length**4 + ((4**4)-certainNum.length**4-1**4)*likelyNum.length;
    // - oのみ - ？のみ
    console.log(combination);
  } else if(certainNum.length === 2) {
    const combination = certainNum.length**4 + ((3**4)*likelyNum.length-certainNum.length**4) + ((4**4)*likelyNum.length*(likelyNum.length-1)-certainNum.length**4);
    console.log(combination);
  } else if(certainNum.length === 1) {
    const combination = certainNum.length**4 + ((2**4)*likelyNum.length-certainNum.length**4) + ((3**4)*likelyNum.length*(likelyNum.length-1)*(likelyNum.length-2)-certainNum.length**4) + ((4**4)*likelyNum.length*(likelyNum.length-1)*(likelyNum.length-2)-certainNum.length**4);
    console.log(combination);
  } else if(certainNum.length === 0) {

  } else console.log(0);

}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
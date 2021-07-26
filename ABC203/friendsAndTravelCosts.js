"use strict";
const main = input => {
  const lines = input.trim().split("\n").map(line => line.split(' '));
  let money = parseInt(lines[0][1]);
  const friends = lines.slice(1);
  friends.sort((a, b) => a[0] - b[0]);
  for(let i=0; i<friends.length; i++) {
    if(money >= parseInt(friends[i][0])) money += parseInt(friends[i][1]);
    else break;
  }
  console.log(money);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
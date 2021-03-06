"use strict";
const main = input => {
  input = input.trim().split("\n");
  const [h, w, n] = input[0].split(" ").map(c => parseInt(c));
  const cards = [];
  for(let i=1; i<=n; i++) {
    const coor = input[i].split(" ").map(c => parseInt(c));
    cards.push([i, ...coor]);
  }
  const rows = {};
  const cols = {};
  cards.sort((a, b) => a[1] - b[1]);
  for(let i=0,r=1; i<n; i++) {
    if(!rows[cards[i][1]]) {
      rows[cards[i][1]] = r;
      r++;
    }
  }
  cards.sort((a, b) => a[2] - b[2]);
  for(let i=0,c=1; i<n; i++) {
    if(!cols[cards[i][2]]) {
      cols[cards[i][2]] = c;
      c++;
    }
  }
  cards.sort((a, b) => a[0] - b[0]);
  cards.forEach(card => {
    console.log(rows[card[1]] + " " + cols[card[2]]);
  })
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
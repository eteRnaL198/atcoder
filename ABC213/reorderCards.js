"use strict";
const main = input => {
  input = input.trim().split("\n");
  const [h, w, n] = input[0].split(" ").map(c => parseInt(c));
  const cards = [];
  for(let i=1; i<=n; i++) {
    const coor = input[i].split(" ").map(c => parseInt(c));
    cards.push([i, ...coor]);
  }
  const cols = {};
  const rows = {};
  cards.forEach(card => {
    rows[card[1]] = true;
    cols[card[2]] = true;
  })
  cards.sort((a, b) => a[1] - b[1]);
  for(let i=0,r=1; i<n; i++) {
    cards[i][1] = r;
    r += typeof cards[i+1] !== 'undefined' && cards[i][1] !== cards[i+1][1] ? 1 : 0;
  }
  cards.sort((a, b) => a[2] - b[2]);
  for(let i=0,c=1; i<n; i++) {
    cards[i][2] = c;
    c += typeof cards[i+1] !== 'undefined' && cards[i][2] !== cards[i+1][2] ? 1 : 0;
  }
  cards.sort((a, b) => a[0] - b[0]);
  cards.forEach(card => {
    console.log(card[1] + " " + card[2]);
  })
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
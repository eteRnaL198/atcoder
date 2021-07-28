"use strict";
const main = input => {
  input = input.trim().split("\n").map(line => line.split(" "));
  const n = parseInt(input[0][0]);
  const roads = input.slice(1);
  let ans = 0;
  const vectors = Array(n+1).fill().map(() => []);
  roads.forEach(road => {
    vectors[road[0]].push(parseInt(road[1]));
  })

  const f = (idx, queue) => {
    if(queue.indexOf(idx) === -1) {
      queue.push(idx);
      ans++;
      vectors[idx].forEach((v) => {
        f(v, queue);
      })
    }
  }

  for(let i=1; i<=n; i++) {
    f(i, []);
  }

  console.log(ans);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
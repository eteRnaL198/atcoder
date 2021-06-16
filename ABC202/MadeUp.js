"user strict";
const main = input => {
  input = input.trim().split('\n');
  const [n, a, b, c] = input.map(val => (
    val.split(' ').map(word => parseInt(word, 10))
  ));
  const a_asce = a.sort((a,b) => a-b);
  const res = [];
  c.forEach(c_val => {
    res[b[c_val-1]] ? res[b[c_val-1]]++ : res[b[c_val-1]] = 1
  })
  let count = 0;
  for(let i=0; i<n; i++) {
    count += res[a_asce[i]] ? res[a_asce[i]] : 0
  }
  console.log(count);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
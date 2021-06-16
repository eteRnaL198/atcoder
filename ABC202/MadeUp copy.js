"user strict";
const main = input => {
  input = input.split('\n');
  input.shift();
  const [a, b, c] = input.map(val => {
    const words = val.split(' ');
    return words.map(word => parseInt(word));
  });
  const combination = a.reduce((count, val) => {
    const b_idx = b.map((b_val, idx) => (
      (b_val === val) ? idx+1 : -1
    ));
    const c_count = b_idx.reduce((acc, val) => {
      const c_applied = c.filter((c_val) => c_val === val)
      return acc + c_applied.length;
    }, 0)
    return count + c_count;
  }, 0);
  console.log(combination);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
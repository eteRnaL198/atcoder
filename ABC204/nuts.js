"use strict";
const main = input => {
  input = input.trim().split("\n");
  const trees = input[1].split(" ");
  const nuts = trees.reduce((acc, tree) => {
    tree = parseInt(tree, 10) - 10;
    return tree > 0 ? acc+tree : acc;
  }, 0);
  console.log(nuts);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
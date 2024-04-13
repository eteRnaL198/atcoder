package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n, t int
	fmt.Scanf("%d %d", &n, &t)

	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	raw_cs := strings.Split(sc.Text(), " ")
	sc.Scan()
	raw_rs := strings.Split(sc.Text(), " ")
	var cs, rs []int
	for i := 0; i < n; i++ {
		c, _ := strconv.Atoi(raw_cs[i])
		cs = append(cs, c)
		r, _ := strconv.Atoi(raw_rs[i])
		rs = append(rs, r)
	}

	//TODO {c1: r1, c2: r2, ...} の構造に変換したい

}

/* 入力例1
4 2
1 2 1 2
6 3 4 5
*/
/* 出力例1
4
*/

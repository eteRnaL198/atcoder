package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var n, k, x int
	fmt.Scanf("%d %d %d", &n, &k, &x)

	var a []int
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	line := strings.Split(sc.Text(), " ")

	for i := 0; i < n; i++ {
		num, _ := strconv.Atoi(line[i])
		a = append(a, num)
	}

	right := make([]int, n-k)
	copy(right, a[k:])

	b := append(append(a[0:k], []int{x}...), right...)

	for _, v := range b {
		fmt.Print(v, " ")
	}
	fmt.Print("\n")
}

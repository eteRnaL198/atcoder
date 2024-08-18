package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var n, k int
	fmt.Scanf("%d %d %d", &n, &k)

	var a []int
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	line := strings.Split(sc.Text(), " ")

	for i := 0; i < n; i++ {
		num, _ := strconv.Atoi(line[i])
		a = append(a, num)
	}
	sort.Slice(a, func(i, j int) bool {
		return a[i] < a[j]
	})

	width := n - k - 1
	diffs := []int{}
	for i := 0; i < n-width; i++ {
		diffs = append(diffs, a[i+width]-a[i])
	}

	sort.Slice(diffs, func(i, j int) bool {
		return diffs[i] < diffs[j]
	})

	fmt.Println(diffs[0])

}

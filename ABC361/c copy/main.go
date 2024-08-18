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

	if k%2 == 0 {
		b := make([]int, n-k)
		b = a[k/2 : n-(k/2)]
		sort.Slice(b, func(i, j int) bool {
			return b[i] < b[j]
		})

		min := b[0]
		max := b[n-k-1]
		fmt.Println(max - min)
		return
	} else {
		left := k / 2
		right := k - left
		b := make([]int, n-k)
		copy(b, a[left:n-right+1])
		sort.Slice(b, func(i, j int) bool {
			return b[i] < b[j]
		})

		min := b[0]
		max := b[n-k-1]
		min1 := max - min

		left, right = right, left
		b2 := make([]int, n-k)
		copy(b2, a[left:n-right+1])
		sort.Slice(b, func(i, j int) bool {
			return b[i] < b[j]
		})

		min = b2[0]
		max = b2[n-k-1]
		min2 := max - min

		if min1 < min2 {
			fmt.Println(min1)
			return
		}
		fmt.Println(min2)
	}

}

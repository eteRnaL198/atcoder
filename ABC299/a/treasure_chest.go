package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int
	var S string
	fmt.Scan(&N)
	fmt.Scan(&S)

	parts := strings.Split(S, "*")
	if len(parts) < 2 {
		fmt.Println("out")
		return
	}
	left := parts[0]
	right := parts[1]

	if strings.Contains(left, "|") && strings.Contains(right, "|") {
		fmt.Println("in")
		return
	}
	fmt.Println("out")
}

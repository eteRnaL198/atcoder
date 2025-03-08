// go run main.go

package main

import "fmt"

func main() {
	val, val2, val3 := "?", "?", "?"
	arr := [][]*string{{&val, &val2, &val3}, {&val, &val2, &val3}, {&val, &val2, &val3}}

	for _, v := range arr {
		for _, v2 := range v {
			fmt.Printf("%v ", *v2)
		}
	}
	fmt.Println()

	val = "x"
	for _, v := range arr {
		for _, v2 := range v {
			fmt.Printf("%v ", *v2)
		}
	}
	fmt.Println()
}

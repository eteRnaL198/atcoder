// go run main.go

package main

import "fmt"

func main() {
	val := 1
	arr := []*int{&val, &val, &val}

	for _, v := range arr {
		fmt.Printf("%v ", *v)
	}
	fmt.Println()

	val = 2
	for _, v := range arr {
		fmt.Printf("%v ", *v)
	}
	fmt.Println()
}

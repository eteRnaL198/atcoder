package main

import (
	"fmt"
)

func main() {
	var a, b, c, d, e, f, g, h, i, j, k, l int
	fmt.Scanf("%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f)
	fmt.Scanf("%d %d %d %d %d %d", &g, &h, &i, &j, &k, &l)

	is_in_x := (a < g && g < d) || (a < j && j < d)
	is_in_y := (b < h && h < e) || (b < k && k < e)
	is_in_z := (c < i && i < f) || (c < l && l < f)

	is_surrounded_x := (g <= a && d <= g) && (j <= a && d <= j)
	is_surrounded_y := (h <= b && e <= h) && (k <= b && e <= k)
	is_surrounded_z := (i <= c && f <= i) && (l <= c && f <= l)

	if (is_in_x || is_surrounded_x) && (is_in_y || is_surrounded_y) && (is_in_z || is_surrounded_z) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

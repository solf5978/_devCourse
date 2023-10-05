package _fullTimeGoDev

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		fmt.Println("Current:", i)
	}

	number := []int{1, 2, 3, 4, 5, 6, 7}

	for i := 0; i < len(number); i++ {
		fmt.Println(i)
		fmt.Println(number[i+1])
	}

	numString := []string{"a", "b", "c", "d"}

	for _, i := range numString {
		fmt.Println(i)
		if i == "c" {
			break
		}
	}
	fmt.Println("Loop End")

	users := map[string]int{
		"foo":   1,
		"bar":   2,
		"baz":   3,
		"alice": 4,
		"bob":   5,
	}

	for key, value := range users {
		fmt.Printf("key %s value %d\n\n", key, value)
	}
}

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
}

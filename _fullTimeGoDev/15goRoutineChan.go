package _fullTimeGoDev

import (
	"fmt"
	"time"
)

func fetchResource(num int) string {
	time.Sleep(time.second * 2)
	return fmt.Sprintf("result %d", num)
}

func main() {
	go fetchResource(1)

	go func() {
		fetchResource(1)
	}()

	result := fetchResource(1)
	fmt.Println("End -> %d", result)
}

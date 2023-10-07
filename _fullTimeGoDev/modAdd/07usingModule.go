package main

import (
	"fmt"
	"math/rand"
)

func main() {
	randNum := getRand()
	fmt.Println(randNum)

	user := User{
		Username: "Jason",
		Age:      getRand(),
	}
	fmt.Printf("USER: %s | Age: %d\n", user.username, user.age)
}

func getRand() int {
	return rand.Int()
}

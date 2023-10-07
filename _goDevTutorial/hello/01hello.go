package main

import (
	"example/greetings"
	"fmt"
	"rsc.io/quote"
)

func main() {
	fmt.Println("Hello, World!")
	fmt.Println(quote.Go())
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}

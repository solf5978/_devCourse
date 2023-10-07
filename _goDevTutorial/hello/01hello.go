package main

import (
	"example/greetings"
	"fmt"
	"log"
	"rsc.io/quote"
)

func main() {

	log.SetPrefix("greetings: ")
	log.SetFlags(0)
	fmt.Println("Hello, World!")
	fmt.Println(quote.Go())
	message, err := greetings.Hello("Gladys")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(message)
}

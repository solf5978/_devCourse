package main

import "fmt"

func main() {
	// Printing globalVar from other go File as long as they are under
	// the same folder layer.
	print(globalVar)
	PrintSome()

	fmt.Println("diff")
}

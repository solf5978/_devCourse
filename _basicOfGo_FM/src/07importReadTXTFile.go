package main

import "fmt"

func main() {
	filename := "Path To The File"

	content, err := src.ReadTextFile(filename)
	if err != nil {
		fmt.Println(content)
	} else {
		fmt.Printf("Panic at %v", err)
	}
}

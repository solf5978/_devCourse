package main

import (
	"fmt"
	"os"
)

func main() {
	parentPath, _ := os.Getwd()
	filename := "Path To The File"

	content, err := ReadTextFile(parentPath + "/" + filename)
	if err != nil {
		fmt.Println(content)
		newContent := "Original: " + content + "\n Double the content"
		newContent = fmt.Sprintf("Original: %v \n double the content", content)
		err := WriteToFile(filename+".output", newContent)
		if err != nil {
			return
		}
	} else {
		fmt.Printf("Panic at %v", err)
	}
}

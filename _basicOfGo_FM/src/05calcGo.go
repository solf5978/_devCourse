package main

import "fmt"

func main() {
	var (
		operation        string
		number1, number2 int
	)

	fmt.Println("Calulator Go 1.0")
	fmt.Println("============================")
	fmt.Println("Which operation do you like to perform? ( + - * //")

	_, err := fmt.Scanf("%s\n", &operation)
	if err != nil {
		return
	}
	fmt.Println("Enter your first number")
	_, err = fmt.Scanf("%d\n", &number1)
	if err != nil {
		return
	}

	fmt.Println("Enter your second number")
	_, err = fmt.Scanf("%d\n", &number2)
	if err != nil {
		return
	}

	switch operation {
	case "add":
		fmt.Println(number1 + number2)
	case "substract":
		fmt.Println(number1 - number2)
	case "multiply":
		fmt.Println(number1 * number2)
	case "divide":
		fmt.Println(number1 / number2)

	}

}

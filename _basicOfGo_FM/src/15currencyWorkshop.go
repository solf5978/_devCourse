package main

import "fmt"

func main() {
	rate, err := GetRate("BTC")
	if err == nil {
		fmt.Println("The rate for %v is %.2f \n", rate.Currency, rate.Price)
	}
	if err != nil {
		return
	}
	print(rate.Price)

}

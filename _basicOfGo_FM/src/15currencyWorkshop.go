package main

func main() {
	rate, err := GetRate("BTC")
	if err != nil {
		return
	}
	print(rate.Price)

}

package main

import (
	"fmt"
	"net/http"
)

func handleHello(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello From A Go Program"))
}

func main() {
	http.HandleFunc(
		"/", handleHello)
	err := http.ListenAndServe(":3333", nil)
	if err != nil {
		return
	} else {
		fmt.Println("No Response From The Server")
	}
}

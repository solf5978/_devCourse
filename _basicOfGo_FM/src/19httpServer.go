package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc(
		"/",
		func (w http.ResponseWriter, r *http.Request) {
			w.Write([]byte("Hello From A Go Program"))
		}
	)
	err := http.ListenAndServe(":3333", nil)
	if err != nil {
		return
	} else {
		fmt.Println("No Response From The Server")
	}
}

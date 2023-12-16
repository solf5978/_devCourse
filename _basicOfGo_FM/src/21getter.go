package main

import (
	"encoding/json"
	"net/http"
	"strconv"

)


func Get(w http.ResponseWriter, r *http.Request) {
	queryString := r.URL.Query()
	id := queryString["id"]
	if id != nil {
		index, err := strconv.Atoi(id[0])
		if err == nil && index < len(List) {
			w.Header().Set("Content-Type", "application/json")
			json.NewEncoder(w).Encode(List[index])
		} else {
			http.Error(w, "Invalid ID", http.StatusBadRequest)
		}
	} else {
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(List))
	}
}

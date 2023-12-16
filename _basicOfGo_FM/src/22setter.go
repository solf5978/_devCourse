package main

import (
	"encoding/json"
	"net/http"
)

func Post(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost {
		var item Exhibition
		err := json.NewDecoder(r.Body).Decode(&item)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		} else {
			append(List, item)
			w.Write([]byte("OK"))
		}
	} else {
		http.Error(w, "Unsupported Method", http.StatusMethodNotAllowed)
	}
}

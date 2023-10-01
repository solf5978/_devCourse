package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"strings"
)

const apiUrl = "https://cex.io/api/ticker/%s/USD"

func GetRate(currency string) (*Rate, error) {
	res, err := http.Get(fmt.Sprintf(apiUrl, strings.ToUpper(currency)))
	if err != nil {
		return nil, err
	}

	if res.StatusCode == http.StatusOK {
		bodyBytes, err2 := io.ReadAll(res.Body)
		if err2 != nil {
			return nil, err2
		}

		var cryptoRate Rate

		err := json.Unmarshal(bodyBytes, &cryptoRate)
		if err != nil {
			return nil, err
		}

	} else {
		return nil, fmt.Errorf("status code received: %v", res.StatusCode)
	}
	rate := Rate{
		Currency: currency,
		Price:    20,
	}

	return &rate, nil
}

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
	if len(currency) != 3 {
		return nil, fmt.Errorf("Currency Format Is Unmatched")
	}
	res, err := http.Get(fmt.Sprintf(apiUrl, strings.ToUpper(currency)))
	if err != nil {
		return nil, err
	}

	var response CEXResponse
	if res.StatusCode == http.StatusOK {
		bodyBytes, err2 := io.ReadAll(res.Body)
		if err2 != nil {
			return nil, err2
		}

		err := json.Unmarshal(bodyBytes, &response)
		if err != nil {
			return nil, err
		}

	} else {
		return nil, fmt.Errorf("status code received: %v", res.StatusCode)
	}
	rate := Rate{
		Currency: currency,
		Price:    response.Bid,
	}

	return &rate, nil
}

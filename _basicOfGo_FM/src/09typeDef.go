package main

// Create an alias for INT
type isInteger = int

var testInt isInteger

type json = map[string]string

// Create a New Type
type distance float64
type distanceKm float64

func test() {
	d := distance(4.5)
	d.toKm()
	print(d)
}
func (miles distance) toKm() distanceKm {
	return distanceKm(1.6093 * miles)
}

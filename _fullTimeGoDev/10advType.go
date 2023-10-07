package _fullTimeGoDev

import "fmt"

type Position struct {
	x, y int
}

type Entity struct {
	name    string
	id      string
	version string
	Position
}

type SpecEntity struct {
	Entity
	specialField float64
}

func main() {
	e := SpecEntity{
		specialField: 1.2,
		Entity: Entity{
			name:    "first entity",
			id:      "id1",
			version: "version 1.1",
			Position: Position{
				x: 100,
				y: 200,
			},
		},
	}
	fmt.Printf("%+v\n", e)
}

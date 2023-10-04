package _fullTimeGoDev

import "fmt"

var name = "Foo"
var firstName string = "Foo"
var lastName string

var (
	firstVar  int = 123
	secondVar int = 456
)

const constantVar string = "this is a constant"
const (
	anotherWay string = "another way 2 declare"
	test123    int    = 12
)

func main() {
	version := 1
	otherVersion := "Bar"
	anotherVersion := "10.5"

	fmt.Println(version)
}

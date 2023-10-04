package _fullTimeGoDev

import "fmt"

var (
	floatVar   float32 = 0.1
	floatVar64 float64 = 0.1
	name       string  = "Foo"
	intVar32   int32   = 1
	intVar64   int64   = 32769
	intVar     int     = 10
	uintVar    uint    = 1
	uintVar32  uint32  = 1
	uintVar64  uint64  = 11212
	uintVar8   uint8   = 0x32
	byteVar    byte    = 0x12
	runeVar    rune    = 'a'
)

type Player struct {
	name        string
	health      int
	attackPower float64
}

func main() {
	player := Player{
		name:        "Captain Jack",
		health:      100,
		attackPower: 45.1,
	}

	fmt.Printf("this is the player: %+v\n", player)
}

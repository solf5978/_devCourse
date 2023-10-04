package _fullTimeGoDev

import "fmt"

var (
	floatVar   float32 = 0.1
	floatVar64 float64 = 0.1
	nameA      string  = "Foo"
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

//  Normal Function
//	func getHealth(player Player) int {
//		return player.health
//	}

// Struct Method
func (player Player) getHealth() int {
	return player.health
}

func main() {
	player := Player{
		name:        "Captain Jack",
		health:      100,
		attackPower: 45.1,
	}

	users := map[string]int{
		// users = make(map[string]int)
	}

	users["foo"] = 1
	users["bar"] = 2

	//	Access Map

	age := users["foo"]
	fmt.Println(age)

	secAge, err := users["hello"]
	if !err {
		fmt.Printf("Age is %d\n", secAge)
	} else {
		fmt.Println("Value is not exist")
	}

	delete(users, "foo")

	fmt.Printf("this is the player: %+v\n", player)
	fmt.Printf("Remain Health: %d\n", player.getHealth())
}

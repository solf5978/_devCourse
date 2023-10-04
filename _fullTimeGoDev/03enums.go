package _fullTimeGoDev

import "fmt"

type WeaponType int

func getDamage(weaponType string) int {
	switch weaponType {
	case "axe":
		return 100
	case "sword":
		return 90
	case "woodenStick":
		return 1
	case "knife":
		return 40
	default:
		panic("Don't get it without a weapon")
	}
}

func main() {
	fmt.Println("damage of weapon:", getDamage("woodenStick"))
}

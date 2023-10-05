package _fullTimeGoDev

import "fmt"

type WeaponType int

const (
	Axe WeaponType = iota
	Sword
	WoodenStick
	Knife
)

func getDamage(weaponType WeaponType) int {
	switch weaponType {
	case Axe:
		return 100
	case Sword:
		return 90
	case WoodenStick:
		return 1
	case Knife:
		return 40
	default:
		panic("Don't get it without a weapon")
	}
}

func main() {
	fmt.Println("damage of weapon (%d) (%d):\n", Axe, getDamage(Axe))
}

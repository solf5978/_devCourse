package main

import "fmt"

type Player struct {
	Health int
}

func TakeDamage(player *Player, amount int) {
	player.Health = player.Health - amount
	fmt.Println("The Player is taking damage. HP :", player.Health)
}

func (p *Player) TakeDamage(amount int) {
	p.Health = p.Health - amount
	fmt.Println("The Plyaer is taking real damage, HP :", p.Health)
}

type BigData struct {
}

func doSTHwData(data BigData) {

}

func main() {
	player := &Player{
		Health: 100,
	}
	player.TakeDamage(10)

	fmt.Printf("%+v\n", player)
}

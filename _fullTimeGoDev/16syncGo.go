package _fullTimeGoDev

import "fmt"

type Server struct {
}

func (s *Server) start() {
	fmt.Println("Starting Server")
}

func (s *Server) loop() {
	for {
		select {}
	}
}

func main() {

}

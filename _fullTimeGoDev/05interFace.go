package _fullTimeGoDev

type StoreOwner interface {
	GetStoreName() ([]int, error)
	SetStoreName()
	DelStoreName()
	UpdateStoreName(int) error
}

type ApiServer struct {
	storeMGR StoreOwner
}

func main() {

}

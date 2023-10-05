package _fullTimeGoDev

type StoreOwner interface {
	GetStoreName() ([]int, error)
	SetStoreName()
	DelStoreName()
	UpdateStoreName(int) error
}

type CandyStoreOwner struct{}

type ApiServer struct {
	storeMGR StoreOwner
}

func (candyO CandyStoreOwner) GetStoreName() ([]int, error) {
	return []int{1, 2, 3}, nil
}

func main() {

}

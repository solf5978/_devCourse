package _fullTimeGoDev

import "fmt"

type StoreOwner interface {
	GetStoreName() ([]int, error)
	SetStoreName()
}

type CandyStoreOwner struct{}

type ApiServer struct {
	storeMGR StoreOwner
}

func (candyO CandyStoreOwner) GetStoreName() ([]int, error) {
	return []int{1, 2, 3}, nil
}

func (candyO CandyStoreOwner) SetStoreName() {
	return
}
func main() {
	storeApi := ApiServer{
		storeMGR: CandyStoreOwner{},
	}

	storeApi.storeMGR.SetStoreName()
	storeName, err := storeApi.storeMGR.GetStoreName()
	if err != nil {
		panic(err)
	}
	fmt.Println(storeName)
}

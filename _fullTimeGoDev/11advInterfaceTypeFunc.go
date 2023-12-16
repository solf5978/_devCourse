package _fullTimeGoDev

import "strings"

type Storage interface {
	Get(id int) (any, error)
	Put(id int, value any) error
}

type TransformFunc func(s string) string

func Uppercase(s string) string {
	return strings.ToUpper(s)
}

func transformString(s string, fn TransformFunc) string {
	return fn(s)
}

type Server struct {
	store Storage
}
type FooStorage struct{}

func (s *FooStorage) Get(id int) (any, error) {
	return nil, nil
}

func (s *FooStorage) Put(id int, value any) error {
	return nil
}

func updateValue(id int, val any) error {
	store := &FooStorage{}
	store.Put(id, val)
	return nil
}

func main() {
	s := &Server{
		store: &FooStorage{},
	}
	getValue, err := s.store.Get(1)
	if err != nil {

	}
	s.store.Put(1, "foo")
}

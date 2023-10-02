package main

import "testing"

// package $PKGNAME_test

func TestAPICall(t *testing.T) {
	_, err := GetRate("")
	if err == nil {
		panic("get nil on error, check the input")
		t.Error("Error was not found")
	}
}

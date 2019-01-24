package main

import (
	"crypto/rand"
	"fmt"
)

func main() {
	for {
		fmt.Print(rand.Int())
	}
}

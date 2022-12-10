package main

import (
	"fmt"
	"os"
)

func main() {

	puzzle := os.Args[1]
	var answer int
	var err error = nil

	switch puzzle {
	case "1a":
		answer, err = day1a("input/1a.txt")
	}

	if err != nil {
		panic(err)
	}
	fmt.Printf("%s: %d\n", puzzle, answer)
}

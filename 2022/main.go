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
		answer, err = day1("input/1.txt", 1)
	case "1b":
		answer, err = day1("input/1.txt", 3)
	case "2a":
		answer, err = day2a("input/2.txt")
	case "2b":
		answer, err = day2b("input/2.txt")
	}

	check_error_panic(err)
	fmt.Printf("%s: %d\n", puzzle, answer)
}

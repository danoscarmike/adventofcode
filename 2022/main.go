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
	case "3a":
		answer, err = day3a("input/3.txt")
	case "3b":
		answer, err = day3b("input/3.txt")
	case "4a":
		answer, err = day4("input/4.txt", "complete")
	case "4b":
		answer, err = day4("input/4.txt", "partial")
	}

	check_error_panic(err)
	fmt.Printf("%s: %d\n", puzzle, answer)
}

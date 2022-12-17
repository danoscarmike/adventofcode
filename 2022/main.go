package main

import (
	"fmt"
	"os"
)

func main() {

	puzzle := os.Args[1]
	var answer interface{}
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
	case "5a":
		answer, err = day5("input/5.txt", false)
	case "5b":
		answer, err = day5("input/5.txt", true)
	case "6a":
		answer, err = day6("input/6.txt", 4)
	case "6b":
		answer, err = day6("input/6.txt", 14)
	case "7a":
		answer, err = day7("input/7.txt", "a")
	case "7b":
		answer, err = day7("input/7.txt", "b")
	case "8a":
		answer, err = day8a("input/8.txt")
	case "8b":
		answer, err = day8b("input/8.txt")
	case "9a":
		answer, err = day9("input/9.txt", 2)
	case "9b":
		answer, err = day9("input/9.txt", 10)
	case "10a":
		answer, err = day10("input/10.txt")
	}

	check_error_panic(err)
	fmt.Println(answer)
}

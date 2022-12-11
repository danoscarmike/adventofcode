package main

import "strings"

func day2a(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	total := 0
	for _, line := range input {
		result := 0
		tokens := strings.Split(line, " ")
		switch tokens[0] {
		case "A": // opp plays rock
			if tokens[1] == "X" {
				result += 4 // 1 for your rock, 3 for the draw
			} else if tokens[1] == "Y" {
				result += 8 // 2 for your paper, 6 for the win
			} else {
				result += 3 // 3 for your scissors, 0 for the loss
			}
		case "B":
			if tokens[1] == "X" {
				result += 1
			} else if tokens[1] == "Y" {
				result += 5
			} else {
				result += 9
			}
		case "C":
			if tokens[1] == "X" {
				result += 7
			} else if tokens[1] == "Y" {
				result += 2
			} else {
				result += 6
			}
		}
		total += result
	}

	return total, nil
}

func day2b(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	total := 0
	for _, line := range input {
		result := 0
		tokens := strings.Split(line, " ")
		switch tokens[0] {
		case "A": // opp plays rock
			if tokens[1] == "X" {
				result += 3 // 3 for your scissors, 0 for the loss
			} else if tokens[1] == "Y" {
				result += 4 // 1 for your rock, 3 for the draw
			} else {
				result += 8 // 2 for your paper, 6 for the win
			}
		case "B":
			if tokens[1] == "X" {
				result += 1 // 1 for rock, 0 for the loss
			} else if tokens[1] == "Y" {
				result += 5 // 2 for paper, 3 for the draw
			} else {
				result += 9 // 3 for scissors, 6 for the win
			}
		case "C":
			if tokens[1] == "X" {
				result += 2 // 2 for paper, 0 for the loss
			} else if tokens[1] == "Y" {
				result += 6 // 3 for scissors, 3 for the draw
			} else {
				result += 7 // 1 for rock, 6 for the win
			}
		}
		total += result
	}

	return total, nil
}

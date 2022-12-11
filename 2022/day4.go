package main

import (
	"strconv"
	"strings"
)

func day4(inputpath string, overlap string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	var total int = 0

	for _, line := range input {
		assignments := strings.Split(line, ",")
		one_str := strings.Split(assignments[0], "-")
		two_str := strings.Split(assignments[1], "-")
		one_low, err := strconv.Atoi(one_str[0])
		check_error_panic(err)
		one_high, err := strconv.Atoi(one_str[1])
		check_error_panic(err)
		two_low, err := strconv.Atoi(two_str[0])
		check_error_panic(err)
		two_high, err := strconv.Atoi(two_str[1])
		check_error_panic(err)

		if overlap == "complete" {
			if (one_low >= two_low && one_high <= two_high) || (two_low >= one_low && two_high <= one_high) {
				total++
			}
		} else {
			if (one_low >= two_low && one_low <= two_high) || (two_low >= one_low && two_low <= one_high) {
				total++
			}
		}
	}

	return total, nil
}

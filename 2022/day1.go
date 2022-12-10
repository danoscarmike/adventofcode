package main

import (
	"strconv"
)

func day1a(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	if err != nil {
		return -1, err
	}
	max := 0
	cals := 0
	for _, token := range input {
		if token == "" {
			if cals > max {
				max = cals
			}
			cals = 0
		} else {
			item, err := strconv.Atoi(token)
			if err != nil {
				return -1, err
			}
			cals += item
		}
	}
	if cals > max {
		max = cals
	}
	return max, err
}

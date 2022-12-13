package main

import (
	"strconv"
	"strings"
)

func day8(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	var forest [][]int

	// create slice of slices of ints
	for _, line := range input {
		numbers_str := strings.Split(line, "")
		numbers_int := make([]int, len(numbers_str))
		for i, s := range numbers_str {
			numbers_int[i], _ = strconv.Atoi(s)
		}
		forest = append(forest, numbers_int)
	}

	// create a binary bitmap of the grid
	// 0 == not visible, 1 == visible
	// initialize first and last slices in forest to all 1
	// initialize first and last indices of all other slices to 1

	// for each slice in forest[1:len(forest)-1] loop over each entry
	// if corresponding bitmap == 1 then skip
	// else (bitmap is 0) then check for visibility from edge in each direction

	// optimization: order the scans from (left | top | right | bottom) according 'quadrant'
	// initialize a flag to track visibility (true if visible from any direction)
	// while flag false:
	// scan from left, top, right, bottom

	// if flag is true, update bitmap

	// iterate over all slices in bitmap counting 1's

	return -1, nil
}

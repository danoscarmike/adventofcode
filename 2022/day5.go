package main

import (
	"strconv"
	"strings"
)

func day5(inputpath string, cm9001 bool) (string, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	// initialize a slice of 9 empty slices
	var matrix [][]rune
	k := 9
	for k > 0 {
		var x []rune
		matrix = append(matrix, x)
		k--
	}

	// populate the matrix with the initial container stacks
	for line := 7; line >= 0; line-- {
		j := 0
		for i := 1; i < len(input[line]); i += 4 {
			if rune(input[line][i]) != 32 {
				matrix[j] = append(matrix[j], rune(input[line][i]))
			}
			j++
		}
	}

	// parse the instruction set
	var insts [][]int
	for line := 10; line < len(input); line++ {
		tokens := strings.Split(input[line], " ")
		quantity, err := strconv.Atoi(tokens[1])
		check_error_panic(err)
		from, err := strconv.Atoi(tokens[3])
		check_error_panic(err)
		to, err := strconv.Atoi(tokens[5])
		check_error_panic(err)
		m := []int{quantity, from, to}
		insts = append(insts, m)
	}

	// execute the instructions
	for _, inst := range insts {
		q := inst[0]
		from_len := len(matrix[inst[1]-1])
		from_stack := &matrix[inst[1]-1]
		to_stack := &matrix[inst[2]-1]

		if cm9001 {
			*to_stack = append(*to_stack, (*from_stack)[from_len-q:]...)
			*from_stack = (*from_stack)[:from_len-q]
		} else {
			for q > 0 {
				from_len := len(matrix[inst[1]-1])
				*to_stack = append(*to_stack, (*from_stack)[from_len-1])
				*from_stack = (*from_stack)[:from_len-1]
				q--
			}
		}
	}

	// pop the top container from each stack
	var tops []string
	for _, stack := range matrix {
		tops = append(tops, string(stack[len(stack)-1]))
	}

	answer := strings.Join(tops[:], "")

	return answer, nil
}

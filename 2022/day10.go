package main

import (
	"fmt"
	"strconv"
	"strings"
)

// func day10(inputpath string) (int, error) {
// 	input, err := readLines(string(inputpath))
// 	check_error_panic(err)

// 	xreg := 1
// 	cycle := 0
// 	cycleMap := make(map[int]int)
// 	crt := make([]string, 40*6)
// 	crt_loc := 0

// 	for _, line := range input {
// 		inst := strings.Split(line, " ")
// 		switch inst[0] {
// 		case "addx":
// 			if sprite_overlap(crt_loc, xreg) {
// 				crt[crt_loc] = "#"
// 			} else {
// 				crt[crt_loc] = "."
// 			}
// 			crt_loc += 1

// 			cycleMap[cycle+1] = xreg

// 			if sprite_overlap(crt_loc, xreg) {
// 				crt[crt_loc] = "#"
// 			} else {
// 				crt[crt_loc] = "."
// 			}
// 			crt_loc += 1

// 			var val int
// 			if val, err = strconv.Atoi(inst[1]); err != nil {
// 				panic(err)
// 			}
// 			xreg += val
// 			cycle += 2

// 		case "noop":

// 			if sprite_overlap(crt_loc, xreg) {
// 				crt[crt_loc] = "#"
// 			} else {
// 				crt[crt_loc] = "."
// 			}
// 			crt_loc += 1
// 			cycle += 1
// 		}
// 		cycleMap[cycle] = xreg
// 		fmt.Println(crt_loc)
// 	}

// 	signalCycles := []int{20, 60, 100, 140, 180, 220}
// 	answer := 0

// 	for _, s := range signalCycles {
// 		answer += (s * cycleMap[s])
// 	}

// 	crt_rows := make([][]string, 6)
// 	for row := range crt_rows {
// 		crt_rows[row] = make([]string, 40)
// 	}

// 	for idx, pixel := range crt {
// 		crt_rows[idx/40][idx%40] = pixel
// 	}

// 	for _, pixel := range crt_rows {
// 		fmt.Println(pixel)
// 	}

// 	return answer, nil
// }

func day10(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	signalCycles := []int{20, 60, 100, 140, 180, 220}
	xreg := 1
	cycleMap := make(map[int]int)
	crt := make([]string, 40*6)

	addx := false
	next_inst := 0
	// loop for each CPU cycle
	for cycle := 1; cycle <= len(crt); cycle++ {
		inst := strings.Split(input[next_inst], " ")
		// if we're in the middle of executing an addx
		if addx {
			if sprite_overlap(cycle-1, xreg) {
				crt[cycle-1] = "#"
			} else {
				crt[cycle-1] = "."
			}
			var val int
			if val, err = strconv.Atoi(inst[1]); err != nil {
				panic(err)
			}
			xreg += val
			cycleMap[cycle] = xreg
			// reset addx flag
			addx = false
			next_inst++
		} else {
			if sprite_overlap(cycle-1, xreg) {
				crt[cycle-1] = "#"
			} else {
				crt[cycle-1] = "."
			}
			switch inst[0] {
			case "addx":
				// set addx flag
				addx = true
				// don't update next_inst
			case "noop":
				next_inst++
			}
			cycleMap[cycle] = xreg
		}
	}

	answer := 0

	for _, s := range signalCycles {
		answer += (s * cycleMap[s])
	}

	crt_rows := make([][]string, 6)
	for row := range crt_rows {
		crt_rows[row] = make([]string, 40)
	}

	for idx, pixel := range crt {
		crt_rows[idx/40][idx%40] = pixel
	}

	for _, pixel := range crt_rows {
		fmt.Println(pixel)
	}

	return answer, nil
}

func sprite_overlap(crt_loc int, sprite_loc int) bool {
	if crt_loc%40 >= sprite_loc-1 && crt_loc%40 <= sprite_loc+1 {
		return true
	} else {
		return false
	}
}

package main

import (
	"strconv"
	"strings"
)

func create_grids(inputpath string) ([][]int, [][]int) {
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
	vis_map := make([][]int, len(forest))

	// initialize first and last slices in forest to all 1
	top_btm := make([]int, len(input[0]))
	for i := 0; i < len(top_btm); i++ {
		top_btm[i] = 1
	}
	vis_map[0] = top_btm
	vis_map[len(forest)-1] = top_btm

	// initialize first and last indices of all other slices to 1
	for j := 1; j < (len(vis_map) - 1); j++ {
		vis_map[j] = make([]int, len(input[0]))
		vis_map[j][0] = 1
		vis_map[j][len(input[0])-1] = 1
	}

	return forest, vis_map
}

func day8a(inputpath string) (int, error) {

	forest, vis_map := create_grids(inputpath)
	// for each slice in forest[1:len(forest)-1] conduct scan left and right
	// the matrix rows
	for k := 1; k < len(forest)-1; k++ {
		visible_l_r(&forest[k], &vis_map[k])
	}

	// scan up and down the matrix columns
	for j := 1; j < len(forest[0])-1; j++ {
		visible_u_d(&forest, &vis_map, j)
	}

	answer := 0
	for row := 0; row < len(vis_map); row++ {
		for col := 0; col < len(vis_map[0]); col++ {
			answer += vis_map[row][col]
		}
	}

	return answer, nil
}

func day8b(inputpath string) (int, error) {
	forest, _ := create_grids(inputpath)
	var forest_cols [][]int
	for i := 0; i < len(forest[0]); i++ {
		forest_cols = append(forest_cols, make([]int, len(forest)))
	}
	for i, row := range forest {
		for j, val := range row {
			forest_cols[j][i] = val
		}
	}

	max_scenic_score := 0

	for row := 0; row < len(forest); row++ {
		for col := 0; col < len(forest[0]); col++ {
			this_tree := forest[row][col]
			right := view(forest[row][col+1:], this_tree, false)
			left := view(forest[row][:col], this_tree, true)
			up := view(forest_cols[col][:row], this_tree, true)
			down := view(forest_cols[col][row+1:], this_tree, false)

			scenic_score := right * left * up * down
			if scenic_score > max_scenic_score {
				max_scenic_score = scenic_score
			}
		}
	}

	return max_scenic_score, nil
}

func view(row []int, this_tree int, invert bool) int {
	score := 0
	has_view := true
	next := 0

	line := make([]int, len(row))
	copy(line, row)

	if invert {
		for i, j := 0, len(line)-1; i < j; i, j = i+1, j-1 {
			line[i], line[j] = line[j], line[i]
		}
	}

	for has_view && next < len(line) {
		tree := line[next]
		if tree < this_tree {
			score++
			next++
		} else {
			score++
			has_view = false
		}
	}
	return score
}

func visible_l_r(trees *[]int, bitmap *[]int) {
	// scan left to right
	tallest := (*trees)[0]
	for idx, tree := range (*trees)[1:len(*trees)] {
		if tree > tallest {
			(*bitmap)[idx+1], tallest = 1, tree
		}
	}

	// scan right to left
	tallest = (*trees)[len(*trees)-1]
	for i := len(*trees) - 2; i > 0; i-- {
		if (*trees)[i] > tallest {
			(*bitmap)[i], tallest = 1, (*trees)[i]
		}
	}
}

func visible_u_d(forest *[][]int, bitmap *[][]int, col int) {
	len_forest := len(*forest)

	// scan top to bottom
	tallest := (*forest)[0][col]
	for i := 1; i < len_forest-1; i++ {
		tree := (*forest)[i][col]
		if tree > tallest {
			(*bitmap)[i][col], tallest = 1, tree
		}
	}

	// scan bottom to top
	tallest = (*forest)[len_forest-1][col]
	for j := len_forest - 2; j > 0; j-- {
		tree := (*forest)[j][col]
		if tree > tallest {
			(*bitmap)[j][col], tallest = 1, tree
		}
	}
}

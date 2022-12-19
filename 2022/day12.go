package main

import (
	"github.com/yourbasic/graph"
)

type Graph map[string]map[string]int

func parseInput(inputpath string) ([][]int, int, int) {
	input, err := readLines(inputpath)
	check_error_panic(err)

	nRows := len(input)
	nCols := len(input[0])
	var start int
	var end int
	inputRows := make([][]int, nRows)
	for i := 0; i < nRows; i++ {
		inputRows[i] = make([]int, nCols)
		for j := 0; j < nCols; j++ {
			nodeVal := int(input[i][j])
			nodeId := (i*nCols + j)
			if nodeVal == 83 { // "S" is ascii code 83
				start = nodeId
				inputRows[i][j] = int('a')
			} else if nodeVal == 69 { // "E" is ascii code 69
				end = nodeId
				inputRows[i][j] = int('z')
			} else {
				inputRows[i][j] = nodeVal
			}
		}
	}
	return inputRows, start, end
}

func day12(inputpath string, part string) (int64, error) {
	grid, start, end := parseInput(inputpath)

	nRows := len(grid)
	nCols := len(grid[0])

	// Create the graph
	g := graph.New(nRows * nCols)

	// anonymous functions to help build the graph's edges
	left := func(row int, col int) {
		if grid[row][col-1] <= grid[row][col]+1 {
			thisNodeId := row*nCols + col
			g.AddCost(thisNodeId, thisNodeId-1, 1)
		}
	}
	right := func(row int, col int) {
		if grid[row][col+1] <= grid[row][col]+1 {
			thisNodeId := row*nCols + col
			g.AddCost(thisNodeId, thisNodeId+1, 1)
		}
	}
	up := func(row int, col int) {
		if grid[row-1][col] <= grid[row][col]+1 {
			thisNodeId := row*nCols + col
			g.AddCost(thisNodeId, thisNodeId-nCols, 1)
		}
	}
	down := func(row int, col int) {
		if grid[row+1][col] <= grid[row][col]+1 {
			thisNodeId := row*nCols + col
			g.AddCost(thisNodeId, thisNodeId+nCols, 1)
		}
	}

	for i := 0; i < nRows; i++ {
		for j := 0; j < nCols; j++ {
			if i == 0 {
				down(i, j)
				if j == 0 {
					right(i, j)
				} else if j == nCols-1 {
					left(i, j)
				} else {
					right(i, j)
					left(i, j)
				}
			} else if i == nRows-1 {
				up(i, j)
				if j == 0 {
					right(i, j)
				} else if j == nCols-1 {
					left(i, j)
				} else {
					right(i, j)
					left(i, j)
				}
			} else {
				up(i, j)
				down(i, j)
				if j == 0 {
					right(i, j)
				} else if j == nCols-1 {
					left(i, j)
				} else {
					right(i, j)
					left(i, j)
				}
			}
		}
	}

	_, dist := graph.ShortestPath(g, start, end)

	switch part {
	case "a":
		break
	case "b":
		for i := 0; i < nRows; i++ {
			for j := 0; j < nCols; j++ {
				if grid[i][j] == 97 {
					new_start := (i * nCols) + j
					_, new_dist := graph.ShortestPath(g, new_start, end)
					if new_dist == -1 {
						continue
					} else if new_dist < dist {
						dist = new_dist
					}
				}
			}
		}
	}

	return dist, nil
}

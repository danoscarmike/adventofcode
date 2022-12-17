package main

import (
	"math"
	"strconv"
	"strings"
)

type Position struct {
	x int
	y int
}

func (p Position) is_equal(q Position) bool {
	if q.x == p.x && q.y == p.y {
		return true
	}
	return false
}

func (p Position) is_adjacent(q Position) bool {
	if p.is_equal(q) {
		return true
	} else if math.Abs(float64(q.x-p.x)) <= 1 && math.Abs(float64(q.y-p.y)) <= 1 {
		return true
	}
	return false
}

func (p *Position) keep_up(q Position) {
	// same row (y is equal)
	// if ahead decrease x, else increase x
	if p.is_adjacent(q) {
		return
	}

	if q.y == p.y {
		if p.x > q.x {
			p.x = q.x + 1
		} else if p.x < q.x {
			p.x = q.x - 1
		}
	} else if q.x == p.x {
		if p.y > q.y {
			p.y = q.y + 1
		} else if p.y < q.y {
			p.y = q.y - 1
		}
	} else {
		if p.x < q.x {
			p.x += 1
		} else {
			p.x -= 1
		}
		if p.y < q.y {
			p.y += 1
		} else {
			p.y -= 1
		}
	}
}

func day9(inputpath string, knots int) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)
	s := Position{0, 0}
	rope := make([]Position, knots)
	for knot := range rope {
		rope[knot] = Position{0, 0}
	}

	Tmap := make(map[Position]int)
	Tmap[s] = 1

	for _, inst := range input {
		motion := strings.Split(inst, " ")
		dir := motion[0]
		var dist int
		if dist, err = strconv.Atoi(motion[1]); err != nil {
			panic(err)
		}
		for dist > 0 {
			switch dir {
			case "R":
				rope[0].x++
			case "L":
				rope[0].x--
			case "U":
				rope[0].y++
			case "D":
				rope[0].y--
			}
			for knot := 1; knot < len(rope); knot++ {
				if rope[knot].is_adjacent(rope[knot-1]) {
					continue
				} else {
					rope[knot].keep_up(rope[knot-1])
				}
			}
			Tmap[rope[knots-1]] += 1
			dist--
		}
	}

	return len(Tmap), nil
}

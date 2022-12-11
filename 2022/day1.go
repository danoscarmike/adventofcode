package main

import (
	"container/heap"
	"strconv"
)

func day1(inputpath string, k int) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)
	h := &IntHeap{}
	heap.Init(h)
	cals := 0
	for _, token := range input {
		if token == "" {
			heap.Push(h, cals)
			if h.Len() > k {
				heap.Pop(h)
			}
			cals = 0
		} else {
			item_int, err := strconv.Atoi(token)
			check_error_panic(err)
			cals += item_int
		}
	}
	// push the last Elf's data (flush the counter)
	heap.Push(h, cals)
	if h.Len() > k {
		heap.Pop(h)
	}

	answer := 0
	for _, val := range *h {
		answer += val
	}

	return answer, nil
}

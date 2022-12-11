package main

func item_priority(i int) int {
	if i < 26 {
		return i + 27
	} else {
		return i - 31
	}
}

func rune_freq(s string) []int {
	freq_map := make([]int, 58)
	for _, r1 := range s {
		freq_map[int(r1)-65]++
	}
	return freq_map
}

func day3a(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	var priority_total int = 0

	for _, line := range input {
		length := len(line)
		comp1 := line[0 : length/2]
		comp2 := line[length/2:]

		// 26 uppercase, 26 lowercase, 6 special characters in between
		c1 := rune_freq(comp1)
		c2 := rune_freq(comp2)

		for i := 0; i < 58; i++ {
			if c1[i] > 0 && c2[i] > 0 {
				priority_total += item_priority(i)
			}
		}
	}

	return priority_total, nil
}

func day3b(inputpath string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	var priority_total int = 0

	line_number := 0
	for line_number < len(input) {
		comp1 := input[line_number]
		comp2 := input[line_number+1]
		comp3 := input[line_number+2]

		c1 := rune_freq(comp1)
		c2 := rune_freq(comp2)
		c3 := rune_freq(comp3)

		for i := 0; i < 58; i++ {
			if c1[i] > 0 && c2[i] > 0 && c3[i] > 0 {
				priority_total += item_priority(i)
			}
		}

		line_number += 3
	}

	return priority_total, nil
}

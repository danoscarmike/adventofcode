package main

func day6(inputpath string, markersize int) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	buffer := []rune(input[0])

	// initialize a slice to hold marker characters
	var marker []rune

	// begin to iterate over the range of all chars
	for i, c := range buffer {
		if len(marker) == 0 {
			marker = append(marker, c)
			continue
		} else {
			// check if the next char is in the slice
			index, dup := contains(marker, c)
			// if it is overwrite the slice to begin at index directly after that char
			// append the new char to the end
			if dup {
				marker = append(marker[index+1:], c)
			} else {
				marker = append(marker, c)
			}
		}
		// if it is not in the slice we've found our set of four
		// return the index of the last char
		if len(marker) == markersize {
			return i + 1, nil
		}
	}

	return -1, nil
}

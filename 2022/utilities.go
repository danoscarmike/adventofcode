package main

func check_error_panic(err error) {
	if err != nil {
		panic(err)
	}
}

func contains(s []rune, c rune) (int, bool) {
	for i, j := range s {
		if j == c {
			return i, true
		}
	}
	return -1, false
}

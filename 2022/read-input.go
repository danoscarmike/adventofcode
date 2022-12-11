package main

import (
	"bufio"
	"os"
)

func readLines(filepath string) ([]string, error) {
	file, err := os.Open(filepath)
	check_error_panic(err)
	defer file.Close()

	var input []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	return input, scanner.Err()
}

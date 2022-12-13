package main

import (
	"strconv"
	"strings"
)

func day7(inputpath string, part string) (int, error) {
	input, err := readLines(string(inputpath))
	check_error_panic(err)

	fs := make(map[string]int)
	var dir_seq []string
	var cur_dir_tree []string

	for _, line := range input {
		args := strings.Split(line, " ")
		if args[0] == "$" {
			if args[1] == "cd" {
				switch args[2] {
				case "..":
					cur_dir_tree = cur_dir_tree[:len(cur_dir_tree)-1]
				case "/":
					if len(cur_dir_tree) == 0 {
						cur_dir_tree = append(cur_dir_tree, "/")
					} else {
						cur_dir_tree = cur_dir_tree[0:1]
					}
				default:
					dir_seq = append(dir_seq, args[2])
					cwd := strings.Join(dir_seq, "/")
					cur_dir_tree = append(cur_dir_tree, cwd)
				}
			}
		} else {
			if args[0] == "dir" {
				continue
			} else {
				if bytes, err := strconv.Atoi(args[0]); err == nil {
					for _, dir := range cur_dir_tree {
						fs[dir] += bytes
					}
				}
			}
		}
	}

	var answer int

	switch part {
	case "a":
		answer = 0
		for _, v := range fs {
			if v <= 100000 {
				answer += v
			}
		}
	case "b":
		answer = 70000000
		available := 70000000 - fs["/"]
		required := 30000000 - available
		for _, dir := range fs {
			if dir > required && dir < answer {
				answer = dir
			}
		}
	}

	return answer, nil
}

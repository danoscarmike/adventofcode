package main

import (
	"strconv"
	"strings"
)

type Item struct {
	id    string
	worry int
}

type Monkey struct {
	number      int
	items       []*Item
	operation   string
	operand     string
	test_div    int
	test_t      *Monkey
	test_f      *Monkey
	inspections int
}

func (m *Monkey) inspect() {
	var op int
	var err error
	if m.operand == "old" {
		op = m.items[0].worry
	} else {
		if op, err = strconv.Atoi(m.operand); err != nil {
			panic(err)
		}
	}

	switch m.operation {
	case "*":
		m.items[0].worry *= op
	case "+":
		m.items[0].worry += op
	}

	m.inspections += 1
}

func (m *Monkey) test(derate_worry bool, divisor_prod int) {
	if derate_worry {
		m.items[0].worry /= 3
	} else {
		m.items[0].worry = m.items[0].worry % divisor_prod
	}

	if m.items[0].worry%m.test_div == 0 {
		m.test_t.items = append(m.test_t.items, m.items[0])
	} else {
		m.test_f.items = append(m.test_f.items, m.items[0])
	}
	m.items = m.items[1:]
}

func day11(inputpath string, derate_worry bool, rounds int) (int, error) {
	input, err := readLines(inputpath)
	check_error_panic(err)

	monkeys := make([]Monkey, 8)
	for idx := range monkeys {
		monkeys[idx] = Monkey{number: idx, inspections: 0}
	}

	monkey_number := -1

	for _, line := range input {
		tokens := strings.Split(strings.TrimLeft(line, " "), " ")
		switch tokens[0] {
		case "Monkey":
			monkey_number++
		case "Starting":
			items_str := tokens[2:]
			for _, val := range items_str {
				val_int, err := strconv.Atoi(strings.Trim(val, ","))
				check_error_panic(err)
				new_item := Item{val, val_int}
				monkeys[monkey_number].items = append(monkeys[monkey_number].items, &new_item)
			}
		case "Operation:":
			monkeys[monkey_number].operation = tokens[4]
			monkeys[monkey_number].operand = tokens[5]
		case "Test:":
			var divisor int
			if divisor, err = strconv.Atoi(tokens[3]); err != nil {
				panic(err)
			}
			monkeys[monkey_number].test_div = divisor
		case "If":
			target_monkey, err := strconv.Atoi(tokens[5])
			check_error_panic(err)
			if tokens[1] == "true:" {
				monkeys[monkey_number].test_t = &monkeys[target_monkey]
			}
			if tokens[1] == "false:" {
				monkeys[monkey_number].test_f = &monkeys[target_monkey]
			}
		}
	}

	divisor_prod := 1
	for _, monkey := range monkeys {
		divisor_prod *= monkey.test_div
	}

	for i := 0; i < rounds; i++ {
		for j := 0; j < len(monkeys); j++ {
			for len(monkeys[j].items) > 0 {
				monkeys[j].inspect()
				monkeys[j].test(derate_worry, divisor_prod)
			}
		}
	}

	first_active := 0
	second_active := 0

	for _, monkey := range monkeys {
		if monkey.inspections > first_active {
			first_active, second_active = monkey.inspections, first_active
		} else {
			if monkey.inspections > second_active {
				second_active = monkey.inspections
			}
		}

	}

	return first_active * second_active, nil

}

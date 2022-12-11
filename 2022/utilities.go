package main

func check_error_panic(err error) {
	if err != nil {
		panic(err)
	}
}

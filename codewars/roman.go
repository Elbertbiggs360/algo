package main

import (
	"fmt"
)

func main() {
	fmt.Println(Decode("MCMXXVII"))
}

func Decode(roman string)(int) {
	var current, final, prev int
	if len(roman)==1 {
		final = getRuneVal(roman)
	}	
	for i:=len(roman)-1; i>=0; i-- {
		current = getRuneVal(string(roman[i]))
		if i+1>=len(roman) {
			final += current
			continue
		}
		prev = getRuneVal(string(roman[i+1]))
		if prev > current {
			final = (final-prev) + (prev-current)
			continue
		}
		if prev == current {
			final += current
			continue
		}
		final += current
	}
	return final
}

func getRuneVal(rune string) (int) {
	switch rune {
		case "M":
			return 1000
                case "D":
                        return 500
                case "C":
                        return 100
                case "L":
                        return 50
                case "X":
                        return 10
                case "V":
                        return 5
                case "I":
                        return 1
                default:
                        return -1
	}
}

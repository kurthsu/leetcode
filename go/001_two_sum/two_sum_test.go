package main

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	var tests = []struct {
		nums   []int
		target int
		result []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
	}
	for _, test := range tests {
		if got := twoSum(test.nums, test.target); !reflect.DeepEqual(got, test.result) {
			t.Errorf("twoSum(%v, %v) = %v", test.nums, test.target, got)
		}
	}
}

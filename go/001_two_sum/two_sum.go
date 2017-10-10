package main

import "fmt"

func twoSum(nums []int, target int) []int {
	res := []int{}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				res = append(res, i, j)
				return res
			}
		}
	}
	return res
}

func main() {
	fmt.Println("hello world")
}

# Q1. Two Sum:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        l = {}
        for index, num in enumerate(nums):
            if target - num in l:
                return index,l[target - num]
            else:
                l[num] = index 
        
            return [0,1]
    

if __name__ == "__main__":

    print("Q1. Two Sum")

    nums = [2,7,11,15]
    target = 9
    print(Solution().twoSum(nums, target))

    print("End of Q1. Two Sum")



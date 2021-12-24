class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = 0 
        for i in set(nums): 
            if nums.count(i) == 1: 
                counter += i
        return counter
        
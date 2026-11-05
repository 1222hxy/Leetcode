class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for i,num in enumerate(nums):
            other = target - num
            if other in cache:
                return [i,cache[other]]

            cache[num] = i
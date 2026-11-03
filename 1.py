class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, x in enumerate(nums):
            req = target - x

            if req in seen:
                return [index,seen[req]]
    
            seen[x] = index

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
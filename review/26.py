# 快慢指针 原地修改
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1

        return slow + 1
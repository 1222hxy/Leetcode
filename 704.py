class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid

        return -1

# 二分查找 注意左闭右开
# 左闭右开要落实 注意left和right的取法 所有地方都要遵循 (mid,left,right)
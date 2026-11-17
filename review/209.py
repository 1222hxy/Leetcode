class Solution:
    # 滑动窗口 / 快慢指针
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        fast = 0
        slow = 0
        my_len = float("inf")
        my_sum = 0

        while fast < len(nums):
            my_sum += nums[fast]

            while my_sum >= target:
                my_len = min(my_len, fast - slow + 1)
                my_sum -= nums[slow]
                slow += 1

            fast += 1
        return my_len if my_len != float("inf") else 0




# 注意 有点像蛄蛹 这里用 while 来处理 slow 向前移动 当不满足条件时快指针再挪动
class Solution2:
    # 滑动窗口 / 快慢指针
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        fast = 0
        slow = 0
        my_min = float("inf")
        my_sum = 0
        while fast < len(nums):
            my_sum += nums[fast]
            while my_sum >= target:
                my_min = min(my_min,fast - slow + 1)
                my_sum -= nums[slow]
                slow += 1
            fast += 1

        return my_min if my_min != float("inf") else 0
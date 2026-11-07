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
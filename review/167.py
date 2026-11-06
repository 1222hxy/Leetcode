class Solution:
    # 双指针
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            my_sum = numbers[left] + numbers[right]
            if my_sum == target:
                return [left+1, right+1]
            elif my_sum > target:
                right -= 1
            elif my_sum < target:
                left += 1
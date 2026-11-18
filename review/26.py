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

# 快慢指针 原地修改
# 注意慢指针的移动顺序 可以自己想一想  00123 这种 应该是发现 !=  之后 慢指针向前挪动一个再修改 而不是 原地不动修改
# 慢指针的位置有信息 因此必须 +1 再写入以免破坏信息
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        read = 0

        while read < len(nums):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

            read += 1

        return write + 1
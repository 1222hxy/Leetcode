class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast = 0
        slow = 0
        max_len = 0
        my_set = set()

        while fast < len(s):
            if s[fast] not in my_set:
                max_len = max(max_len, fast - slow + 1)
                my_set.add(s[fast])
                fast += 1
            else:
                my_set.remove(s[slow])
                slow += 1

        return max_len




# 双指针的while写法 while可以处理较为复杂的逻辑
# 注意指针何时变化 此时右指针承载了信息 因此必须操作保存后再 +1
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_set = set()
        max_len = 0

        while right < len(s):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1

            my_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
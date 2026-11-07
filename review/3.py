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
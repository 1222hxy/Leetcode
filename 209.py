class Solution:
    # 滑动窗口 / 快慢指针
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow = 0
        fast = 0
        my_sum = 0
        min_len = float("inf")

        while fast<len(nums):
            my_sum += nums[fast]

            while my_sum >= target:
                min_len = min(min_len, fast - slow + 1)
                my_sum -= nums[slow]
                slow += 1

            fast += 1

        return min_len if min_len != float("inf") else 0


# 滑动窗口: 不满足条件, 快指针往前探路. 满足条件, 慢指针开始起步.

class Solution2:
    # 滑动窗口 / 快慢指针
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        slow = 0
        fast = 0
        my_sum = 0
        my_len = float("inf")

        while fast < len(nums):
            my_sum += nums[fast]

            while my_sum >= target:
                my_len = min(my_len,fast - slow + 1)
                my_sum -= nums[slow]
                slow += 1

            fast += 1

        return my_len if my_len != float("inf") else 0




"""
滑动窗口 (Sliding Window) 是一种基于双指针 (Two Pointers) 的算法技巧, 
主要用于解决数组或字符串中连续区间的相关问题.

其核心思想是使用左右两个指针维护一个动态窗口, 通过移动右指针来扩张窗口, 
移动左指针来收缩窗口, 并在适当时机更新最优解. 根据窗口大小是否固定, 
滑动窗口可以分为固定长度滑动窗口 (Fixed-size Sliding Window) 和
可变长度滑动窗口 (Variable-size Sliding Window).

滑动窗口的本质是利用相邻窗口之间的重叠信息, 避免重复计算和暴力枚举.
在满足相应单调性等条件时, 左右指针均只向前移动而不回退, 
每个指针最多移动 n 次, 因此即使存在嵌套循环, 
整体时间复杂度通常仍为 O(n), 而不是 O(n^2).
这种复杂度分析体现了均摊分析 (Amortized Analysis) 的思想.

滑动窗口的空间复杂度取决于维护窗口状态所使用的数据结构.
如果只维护窗口和、长度等变量, 空间复杂度为 O(1).
如果需要使用哈希表 (Hash Map) 或集合 (Set) 记录窗口元素,
则空间复杂度取决于所存储的不同元素数量.

滑动窗口的关键在于确定窗口的扩张条件、收缩条件以及答案的更新时机.
对于寻找最短合法子数组的问题, 通常在窗口满足条件时更新答案并尝试收缩.
对于寻找最长合法子数组的问题, 通常在窗口不满足条件时收缩,
恢复合法状态后再更新答案.

需要注意, 滑动窗口并不适用于所有连续区间问题.
例如, LeetCode 209 的标准解法依赖数组元素为正整数,
因为此时窗口和随着右指针扩张而增加, 随着左指针收缩而减少.
如果存在负数, 这种单调性可能被破坏, 标准滑动窗口算法就可能失效.
"""


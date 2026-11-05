class Solution:
    # 双指针
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left != right:
            my_sum = numbers[left] + numbers[right]
            if my_sum == target:
                return [left + 1,right + 1]
            elif my_sum > target:
                right -= 1
            elif my_sum < target:
                left += 1


# 有序数组 两个数满足制约条件 -> 双指针

"""
双指针 (Two Pointers)

1. 基本概念 (Definition)
双指针是一种常见的算法技巧, 通过维护两个指针来遍历数据,
利用指针之间的关系减少不必要的计算, 从而提高算法效率.
双指针不一定是两个独立的变量, 也可以是两个下标.

2. 常见类型 (Types)
(1) 相向双指针 (Opposite-Direction Two Pointers):
    两个指针分别从序列两端出发, 逐渐向中间靠拢.
    常用于有序数组的两数之和, 回文判断等问题.

(2) 同向双指针 (Same-Direction Two Pointers):
    两个指针从同一方向出发, 以不同速度或不同条件移动.
    常用于数组去重, 快慢指针, 滑动窗口等问题.

3. 核心思想 (Core Idea)
双指针的核心思想是缩减搜索空间 (Search Space Reduction).
通过利用数据的有序性或其他约束条件, 每次移动指针时,
排除一部分不可能的候选解, 避免重复或无效的计算.

4. 典型例子 (Two Sum II)
对于一个升序数组, 设置 left 和 right 两个指针,
分别指向数组的第一个元素和最后一个元素.

如果 nums[left] + nums[right] < target:
    说明当前和太小, 移动 left 向右寻找更大的数.

如果 nums[left] + nums[right] > target:
    说明当前和太大, 移动 right 向左寻找更小的数.

如果 nums[left] + nums[right] == target:
    说明找到目标解, 返回对应下标.

正确性依据:
当当前和小于 target 时, 由于数组有序,
nums[left] 与当前范围内其他元素相加只会更小,
因此可以安全排除 nums[left].

同理, 当当前和大于 target 时,
可以安全排除 nums[right].

5. 复杂度分析 (Complexity Analysis)
时间复杂度 (Time Complexity): O(n)
每次循环至少有一个指针向中间移动,
最多进行 n - 1 次移动.

空间复杂度 (Space Complexity): O(1)
只需要维护两个指针和少量辅助变量,
不需要额外的数据结构.

6. 适用条件 (When to Use)
双指针特别适合具有以下特点的问题:
(1) 数组已经排序, 可以利用元素之间的大小关系.
(2) 需要寻找满足某种条件的元素对.
(3) 可以通过移动指针安全地排除候选解.
(4) 需要原地处理数组, 降低额外空间开销.

注意: 双指针并不要求数组一定有序.
是否能够使用双指针, 关键在于能否建立正确的指针移动规则.

7. 面试总结 (Interview Summary)
双指针是一种通过维护两个指针来优化搜索或遍历过程的算法技巧.
它的关键不仅在于减少循环次数, 更在于利用问题的约束条件,
证明每次指针移动都不会遗漏有效解.

在满足相应条件时, 双指针可以将某些 O(n^2) 的暴力搜索
优化为 O(n), 同时将额外空间复杂度控制在 O(1).
"""
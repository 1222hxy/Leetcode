class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        read = 0
        write = 0

        while read < len(nums):
            if nums[read] == nums[write]:
                read += 1

            else:
                write += 1
                nums[write] = nums[read]

        return write + 1


"""
双指针 (Two Pointers) - 有序数组原地去重

1. 核心思想 (Core Idea)
   利用有序数组中重复元素相邻的性质, 通过快慢双指针
   (Fast and Slow Pointers) 实现原地去重 (In-place Deduplication).

2. 指针职责 (Pointer Responsibilities)
   - read: 读指针, 负责遍历数组, 寻找新的不重复元素.
   - write: 写指针, 指向最后一个已保留的不重复元素.
   - nums[0:write+1]: 有效前缀, 保存已处理的不重复元素.

3. 算法流程 (Algorithm)
   - 初始化 read = write = 0.
   - 若 nums[read] == nums[write], 移动 read.
   - 否则, 移动 write, 并将 nums[read] 写入 nums[write].
   - 赋值后两者必然相等, 因此下一轮自动移动 read.
   - 遍历结束后返回 write + 1.

4. 正确性 (Correctness)
   - Sorted Property: 重复元素相邻, 无需回头检查.
   - Loop Invariant: 有效前缀始终保存已处理的不重复元素.
   - Order Preservation: 保留原有元素的相对顺序.
   - In-place Modification: 直接覆盖原数组, 无需辅助数组.

5. 复杂度分析 (Complexity Analysis)
   - Time Complexity: O(n), 每个元素最多处理常数次.
   - Space Complexity: O(1), 只使用两个指针变量.

6. 边界情况 (Edge Cases)
   - Single Element: 返回 1.
   - All Elements Equal: 返回 1.
   - All Elements Distinct: 返回 n.
   - Empty Array: 原写法返回 1, 需额外处理 (题目保证非空).
   - Unsorted Array: 不能保证正确去重.

7. 常见面试追问 (Follow-up Questions)
   Q1: 为什么返回 write + 1?
   A: write 是从 0 开始的索引, 返回值是有效元素数量.

   Q2: 为什么不删除数组后面的元素?
   A: 题目只要求前 k 个元素正确, 剩余元素无需处理.

   Q3: 为什么不使用 Set?
   A: Set 通常需要 O(n) 额外空间, 而双指针只需要 O(1).

   Q4: 为什么 else 中不需要 read += 1?
   A: 赋值后 nums[read] == nums[write], 下一轮必然移动 read.

   Q5: 这种双指针与左右指针有什么区别?
   A: 快慢指针通常同向移动, 适合原地修改和有效区域维护;
      左右指针通常从两端向中间移动, 适合有序数组查找与配对.

8. 通用思维模型 (General Pattern)
   - Read Pointer: 负责扫描和判断.
   - Write Pointer: 负责保留和覆盖.
   - Valid Prefix: 维护已经处理完成的有效区域.

总结:
   Read 负责寻找, Write 负责维护.
   利用有序性, 通过原地覆盖实现稳定去重.
   时间复杂度 O(n), 额外空间复杂度 O(1).
"""
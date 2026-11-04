class Solution0:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index, x in enumerate(nums):
            req = target - x

            if req in seen:
                return [index,seen[req]]
    
            seen[x] = index


class Solution1:
    # 递归
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i,item in enumerate(nums):
            for j in range(i+1,len(nums)):
                post = nums[j]
                if item + post == target:
                    return [i,j]


#哈希表 记忆功能 遍历一次 记住 数字和它对应的下标

class Solution2:
    # 哈希表
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}

        for i,item in enumerate(nums):
            cache[item] = i

        for i,item in enumerate(nums):
            other = target - item
            if other in cache and cache[other] != i: #补丁：不能取同一个数
                return [i,cache[other]]

class Solution3:
    # 哈希表：省去一次遍历 -> 一边记忆 一边遍历查表
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}
        for i,item in enumerate(nums):
            other = target - item
            if other in cache:
                return [i,cache[other]]

            cache[other] = i

            

"""
哈希表 (Hash Table) 是一种基于键值对 (Key-Value) 存储数据的数据结构.

其核心原理是通过哈希函数 (Hash Function), 将键 (Key) 映射到
哈希表中的存储位置, 从而实现高效的数据查找, 插入和删除.

时间复杂度 (Time Complexity):
1. 查找 (Search): 平均 O(1), 最坏 O(n).
2. 插入 (Insert): 平均 O(1), 最坏 O(n).
3. 删除 (Delete): 平均 O(1), 最坏 O(n).

哈希冲突 (Hash Collision):
当不同的 Key 经过哈希映射后, 对应到相同的存储位置时,
就会产生哈希冲突.

常见的冲突解决方法:
1. 链地址法 (Separate Chaining):
   将映射到同一位置的元素组织在同一个桶中, 通常使用链表等结构.

2. 开放寻址法 (Open Addressing):
   当发生冲突时, 按照一定的探测规则寻找其他可用位置.

Python 中的哈希表:
1. dict: 通过 Key-Value 实现数据映射.
2. set: 基于哈希实现元素去重和快速成员查询.

典型应用场景 (Applications):
1. 快速查找 (Fast Lookup).
2. 数据去重 (Deduplication).
3. 频率统计 (Frequency Counting).
4. 缓存设计 (Caching).
5. 两数之和 (Two Sum).

总结 (Summary):
哈希表是一种典型的以空间换时间 (Space-Time Tradeoff) 的数据结构.
它利用哈希函数实现平均 O(1) 的查找, 插入和删除操作.
其性能主要取决于哈希函数的设计, 哈希冲突的处理方式以及负载因子
(Load Factor), 是算法设计与实际工程中常用的数据结构.
"""
class Solution(object):
    # Brute Force Solution O(N^2)
    def twoSum(self, nums, target):
        for i in nums:
            new_list = [x for x in nums if x != i]
            for j in new_list:
                if i + j == target:
                    index1, index2 = nums.index(i), nums.index(j)
                    return index1, index2


print Solution().twoSum([3,2,4], 6)

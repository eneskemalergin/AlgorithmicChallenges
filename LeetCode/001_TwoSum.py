class Solution(object):
    # Brute Force Solution O(N^2)
    def bruteF_twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range((1+i), len(nums)):
                if nums[j] == target - nums[i]:
                    return i,j
        return "No two sum solution"

    def twoSum(self, nums, target):
        hash_map = {}
        # Fill the hash map
        for ind, val in enumerate(nums):
            hash_map[val] = ind

        for ind1, val in enumerate(nums):
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind1!=ind2:
                    return ind1, ind2
        return "No two sum solution"

print Solution().twoSum([3,2,4], 6)

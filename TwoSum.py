class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            # d[nums[i]] = i
            if target - nums[i] in d and i != d[target - nums[i]]:
                return [i, d[target - nums[i]]]
            d[nums[i]] = i
        return None
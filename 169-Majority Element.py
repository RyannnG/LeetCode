# from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # time and space O(n)
        # d = defaultdict()
        # for i in nums:
        #     d.setdefault(i, 0)
        #     d[i] += 1

        # return max(d.iteritems(), key=operator.itemgetter(1))[0]
        
        # Moore Voting
        # time O(n), space O(1)
        idx = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[idx] == nums[i]:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                idx = i
                count = 1
                
        return nums[idx]
from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict()
        for i in nums:
            d.setdefault(i, 0)
            d[i] += 1

        return max(d.iteritems(), key=operator.itemgetter(1))[0]
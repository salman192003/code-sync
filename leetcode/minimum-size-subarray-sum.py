class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        minw = 999999

        total = 0

        for right in range(len(nums)):

            total = total + nums[right]

            while total >= target:
                minw = min(right - left + 1, minw)
                total = total - nums[left]
                left = left + 1    

        #no such subarray
        if minw==999999:
            return 0

        return minw
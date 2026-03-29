class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        #making the prefix sum array

        sum_array = nums

        sum_array[0] = nums[0]

        for i in range(1,len(nums)):
            sum_array[i] = nums[i] + sum_array[i - 1]
        
        # now to find the number of CONTIGUOUS Subarrays which are a multiple of k

        hashmap = {0: -1}

        for i in range(len(nums)):
            R = sum_array[i] % k
            if R not in hashmap:
                hashmap[R] = i
                
            elif i - hashmap[R] >= 2:
                return True
        
        return False
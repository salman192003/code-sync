class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sumarray = nums
        

        for i in range(1, len(nums)):
            sumarray[i] = sumarray[i-1] + nums[i]

        result = 0

        for i in range(len(sumarray)):
            for j in range(i,len(sumarray)):
                if i == 0:
                    subarray_sum = sumarray[j]
                else:
                    subarray_sum = sumarray[j] - sumarray[i-1]

                if subarray_sum % k == 0:
                    result = result + 1

                
        return result
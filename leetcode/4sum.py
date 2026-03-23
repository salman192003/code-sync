class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        n = len(nums)

        for i in range(len(nums) - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range( i + 1 , len(nums) - 2):

                if j > i + 1 and nums[j] == nums[ j - 1]:
                    continue

                k = j + 1
                l = n-1

                while (k < l):
                    if (nums[i] + nums[j] + nums[k] + nums[l]) < target:
                        k = k + 1
                    elif ( nums[i] + nums[j] + nums[k] + nums[l]) > target:
                        l = l - 1
                    else:
                        res = [nums[i],nums[j],nums[k],nums[l]]
                        result.append(res)
                        k = k + 1
                        l = l - 1
                        
                        while k < l and nums[k] == nums[k - 1]:
                            k = k + 1
                        
                        while k < l and nums[l] == nums[l + 1]:
                            l = l - 1              

        return result
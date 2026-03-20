class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """


        k = 0
        left = 0
        right = len(nums) - 1

        while ( left <= right):

            while left <= right and nums[left] != val:
                left = left + 1

            while right >= 0  and nums[right] == val:
                right = right - 1

            if (left <= right):

                nums[left],nums[right] = nums[right],nums[left]

                left = left + 1

                right = right - 1
            
        return right + 1
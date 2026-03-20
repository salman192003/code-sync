class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            elif nums[i] == 2:
                blue += 1

        for i in range(len(nums)):
            if red:
                nums[i] = 0
                red = red - 1
            elif white:
                nums[i] = 1
                white = white - 1
            elif blue:
                nums[i] = 2
                blue = blue  - 1

        return nums
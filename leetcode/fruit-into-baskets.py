class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """

        left = 0
        counts = {}
        max_c = 0

        for right in range(len(fruits)):
            
            counts[fruits[right]] = counts.get(fruits[right], 0) + 1

            while len(counts) > 2:
                counts[fruits[left]] = counts[fruits[left]] - 1
                
                if counts[fruits[left]] == 0:
                    counts.pop(fruits[left])
                
                left = left + 1

            max_c = max(max_c , right - left + 1)

        return max_c
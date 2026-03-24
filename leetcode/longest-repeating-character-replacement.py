class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        #declaring a 26 character dict maintaing counts
        counts = {}
        
        for i in range(26):
            char = chr(ord('A') + i)
            counts[char] = 0

        left = 0

        max_w = 0

        for right in range (len(s)):
            
            counts[s[right]] = counts[s[right]] + 1

            #not valid window
            while (right - left + 1) - max(counts.values()) > k and left < len(s) :
                #reduce window size
                counts[s[left]] = counts[s[left]] - 1
                left = left + 1

            max_w = max(max_w, right - left + 1)

        return max_w
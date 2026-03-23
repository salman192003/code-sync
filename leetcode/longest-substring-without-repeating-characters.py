class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substr = set()
        max_sub=0

        l= 0

        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l = l + 1

            substr.add(s[r])

            max_sub = max(max_sub, r - l + 1)

        return max_sub
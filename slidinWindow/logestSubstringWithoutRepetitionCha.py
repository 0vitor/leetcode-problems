class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        repetitions = 0
        j = 0
        i = 0
        n = len(s)
        while j < n:


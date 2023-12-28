class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iS = 0
        lenS = len(s)
        if not s: return True

        for tChar in t:
            if tChar == s[iS]:
                iS += 1

            if iS == lenS: return True

        return False

print(Solution().isSubsequence(input(), input()))

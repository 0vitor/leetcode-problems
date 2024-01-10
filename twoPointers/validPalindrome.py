class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for c in s:
            n = ord(c.lower())
            difference = n - 97
            if difference >= 0 and difference <= 25 or difference <= (-40) and difference >= -49:
                a.append(n)

        r = len(a) - 1
        l = 0
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1

        return True


print(Solution().isPalindrome("0a9999aa0"))

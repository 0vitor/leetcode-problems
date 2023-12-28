class Solution:
    def reverseVowels(self, s: str) -> str:
        lHalf: int = 0
        rHalf: int = len(s) - 1
        newS = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']

        while(lHalf < rHalf):
            leftSideIsVowel = s[lHalf].lower() in vowels

            if not leftSideIsVowel:
                lHalf += 1

            rightSideIsVowel = s[rHalf].lower() in vowels

            if not rightSideIsVowel:
                rHalf -= 1

            if leftSideIsVowel and rightSideIsVowel:
                newS[lHalf], newS[rHalf] = newS[rHalf], newS[lHalf] 
                lHalf += 1
                rHalf -= 1

        return ''.join(newS)

n = Solution()
print(n.reverseVowels('fello'))

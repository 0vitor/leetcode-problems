class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        curr_sum = s[0:k]
        maxAmoutVowels = 0
        currentAmountVowels = 0

        for c in curr_sum:
            currentAmountVowels += c in vowels
        maxAmoutVowels = currentAmountVowels

        for i in range(0, len(s) - k):
            if s[i] in vowels:
                currentAmountVowels -= 1
            if s[i+k] in vowels:
                currentAmountVowels += 1
            
            if currentAmountVowels > maxAmoutVowels:
                maxAmoutVowels = currentAmountVowels

        return maxAmoutVowels

str = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
print(Solution().maxVowels(str, 33))


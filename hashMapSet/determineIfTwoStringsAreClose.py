class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        char1Repetitions=[0]*26
        char2Repetitions=[0]*26
        for i in word1:
            char1Repetitions[ord(i)-97]+=1
        for i in word2:
            char2Repetitions[ord(i)-97]+=1
        for i in range(26):
            if (char1Repetitions[i]>0 and char2Repetitions[i]==0) or (char1Repetitions[i]==0 and char2Repetitions[i]>0):
                return False

        char1Repetitions.sort()
        char2Repetitions.sort()

        return char1Repetitions[:] == char2Repetitions[:]


print(Solution().closeStrings("abbzccca", "babzzczc"))

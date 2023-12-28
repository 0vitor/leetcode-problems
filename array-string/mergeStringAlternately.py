class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minorLengthWord: int = len(word1) if len(word1) < len(word2) else len(word2)
        newString: str
        for i in range(0, minorLengthWord):
            newString = newString + word1[i] + word2[i]
        return newString
solucao = Solution()
resultado = solucao.mergeAlternately("abc", "123333")
print(resultado)

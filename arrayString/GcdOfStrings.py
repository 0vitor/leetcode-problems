class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        largestSubstring = str2

        while(largestSubstring):
            largestSubstringLen = len(largestSubstring)            

            if(len(str1) % largestSubstringLen == 0 and len(str2) % largestSubstringLen == 0):
                start = 0
                end = 1 
                print(largestSubstring)
                divisebleStr1 = False
                divisebleStr2 = False

                while(largestSubstringLen*end <= len(str1) or largestSubstringLen <= len(str2)):
                    sliceStr1 = str1[largestSubstringLen*start:largestSubstringLen*end]
                    sliceStr2 = str2[largestSubstringLen*start:largestSubstringLen*end]

                    if((not divisebleStr1 and sliceStr1 != largestSubstring) or (not divisebleStr2 and sliceStr2 != largestSubstring)):
                        break

                    if(largestSubstringLen*end == len(str2)):
                        divisebleStr2 = True

                    if(largestSubstringLen*end == len(str1)):
                        divisebleStr1 = True
                    
                    if(divisebleStr1 and divisebleStr2):
                        return largestSubstring

                    start += 1
                    end += 1


            largestSubstring = largestSubstring[:-1]

        return largestSubstring

solucao = Solution()
str1 = input()
str2 = input()
resultado = solucao.gcdOfStrings(str1, str2)
print(resultado)

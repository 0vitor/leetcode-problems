class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1Repetitions = {}
        word2Repetitions = {}
        wordRepetitions = {}
        if len(word1) != len(word2): return False

        for char in word1:
            if word1Repetitions.get(char):
                word1Repetitions[char] += 1
            else:
                word1Repetitions[char] = 1
        
        for char in word2:
            if word2Repetitions.get(char):
                word2Repetitions[char] += 1
            else:
                word2Repetitions[char] = 1
        
        for key, value in word1Repetitions.items():
            if wordRepetitions.get(value):
                wordRepetitions[value].add(key)
            else:
                wordRepetitions[value] = set(key)

        for key, value in word2Repetitions.items():
            
            amountRepetition = word2Repetitions.get(key)
            charArray = wordRepetitions.get(amountRepetition)

            while word2Repetitions.get(key) != word1Repetitions.get(key) and charArray:
                char = charArray.pop()
                if word2Repetitions.get(char):
                    word2Repetitions[key], word2Repetitions[char]  = word2Repetitions[char], word2Repetitions[key]
                amountRepetition = word2Repetitions.get(key)
                charArray = wordRepetitions.get(amountRepetition)

        for key, value in word2Repetitions.items():
            if value != word1Repetitions[key]:
                print(key, value, word1Repetitions[key])
                return False

        return True

print(Solution().closeStrings("zzazicgvzwntnneauziwfzlrzkynzschzdkbmpqbolwgvxjava", "uequrwuzhaudmnuqjuolkeszcyfqzqizrdrxpuvuygytbucwog"))

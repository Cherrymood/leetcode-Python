class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:

        answer = 0
        result = 0

        for index in range(len(sentences)):
            splitted = sentences[index].split()
            answer = len(splitted)
            if result < answer:
                result = answer
                answer = 0
            else:
                answer = 0

        return result


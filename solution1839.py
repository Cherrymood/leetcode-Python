from collections import OrderedDict

class Solution:
    def sortSentence(self, s: str) -> str:

        s_list: list = s.split()
        dict_s: dict = {}
        answer_list: list = []

        for index in range(len(s_list)):
            dict_s[s_list[index][len(s_list[index])-1]] = s_list[index][0:len(s_list[index])-1]

        dict1 = OrderedDict(sorted(dict_s.items()))

        for value in dict1.values():
            answer_list.append(value)

        answer: str = " ".join(answer_list)

        return answer

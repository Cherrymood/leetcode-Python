class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        alhabet: str = 'abcdefghijklmnopqrstuvwxyz'
        key_1: str = "".join(key.split())
        unic_key: str = ""

        dict_alpha_key = {}
        answer = ""

        for index in range(len(key_1)):
            if key_1[index] in unic_key:
                continue
            else:
                unic_key += key_1[index]

        for index in range(len(alhabet)):
            dict_alpha_key[unic_key[index]] = alhabet[index]

        for index in range(len(message)):
            if message[index] == " ":
                answer += " "
            else:
                answer += dict_alpha_key[message[index]]

        return answer


class Solution:
    def interpret(self, command: str) -> str:

        answer: str = ""

        for index in range(len(command)):
            if command[index] == "G":
                answer += "G"
            elif command[index] == "(" and command[index+1] == "a":
                answer += "al"
            elif command[index] == "(" and command[index+1] == ")":
                answer += "o"
            else:
                continue

        return answer


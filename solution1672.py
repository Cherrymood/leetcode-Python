class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:

        welth = []

        for sub_list in accounts:
            welth.append(sum(sub_list))

        welth.sort(reverse=True)

        return welth[0]










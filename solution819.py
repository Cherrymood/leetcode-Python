class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        p = paragraph.lower()
        p = p.replace('!', ' ')
        p = p.replace('?', ' ')
        p = p.replace("'", ' ')
        p = p.replace(',', ' ')
        p = p.replace(';', ' ')
        p = p.replace('.', ' ')
        l = p.split()

        for i in range(len(l)):
            l[i] = l[i].strip()

        d = dict(Counter(l))
        sorted_d = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))
        for i in sorted_d:
            if i not in banned:
                return i
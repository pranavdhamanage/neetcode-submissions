class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for w in strs:
            s += str(len(w)) + '?' + w

        return s
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            str_length = ""
            while s[i] != '?':
                str_length += s[i]
                i += 1

            res.append(s[i + 1: int(str_length) + i + 1])
            i = int(str_length) + i + 1

        return res
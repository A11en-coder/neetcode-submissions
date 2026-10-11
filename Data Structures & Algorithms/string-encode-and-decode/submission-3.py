class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # we need another pointer to check if the next char is delimeter
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:length+j+1])
            i = j + length + 1
        return res

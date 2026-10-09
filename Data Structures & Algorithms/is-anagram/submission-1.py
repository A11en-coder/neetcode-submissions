class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # check if the length of the str are equal
        if len(s) != len(t):
            return False

        # initialize the hashmaps
        countT, countS = {}, {}
        
        # populate hashmaps
        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)

        # check if the corresponding values in hashmaps are equal
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
        
        

        
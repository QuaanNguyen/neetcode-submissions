class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)

        for i in range(len(t)):
            if t[i] in s:
                s.remove(t[i])
            else:
                return False
        if len(s) > 0:
            return False
        return True
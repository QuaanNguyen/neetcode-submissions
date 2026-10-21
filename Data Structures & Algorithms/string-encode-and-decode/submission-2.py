class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for word in strs:
            x = str(len(word)) + "#" + word
            en += x
        return en

    def decode(self, s: str) -> List[str]:
        i = 0
        de = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            de.append(word)
            i = j+1+length
        return de
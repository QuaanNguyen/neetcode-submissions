class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        brac_dict = {
            '{': '}',
            '[':']',
            '(':')',
        }
        storage = []
        for i in range(len(s)):
            if s[i] in brac_dict.keys():
                storage.append(brac_dict[s[i]])
                print(storage)
            else:
                if len(storage) == 0:
                    return False
                elif s[i] == storage[-1]:
                    storage.pop()
                else:
                    return False
        if len(storage) > 0:
            return False
        return True
        
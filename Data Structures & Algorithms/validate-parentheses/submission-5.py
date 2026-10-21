class Solution:
    def isValid(self, s: str) -> bool:
        brac_dict = {
            '{': '}',
            '[':']',
            '(':')',
        }
        storage = []
        for i in s:
            if i in brac_dict:
                storage.append(i)
            else:
                if storage and brac_dict[storage[-1]] == i:
                    storage.pop()
                else:
                    return False
        return True if not storage else False
        
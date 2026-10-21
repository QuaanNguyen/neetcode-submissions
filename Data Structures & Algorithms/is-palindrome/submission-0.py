class Solution:
    def isPalindrome(self, s: str) -> bool:
    #1. lowercase the input
    #2. characters are good, ignore the space
    #3. length=1, return true
    #4. use .replace(' ', '')
    #5. inverse array[::-1]
        newArray = []
        s = s.lower()
        # Pre-processing step
        for char in s:
            if char.isalnum():
                newArray.append(char)
            else:
                continue
        # Check
        if newArray == newArray[::-1]:
            return True
        else:
            return False
    
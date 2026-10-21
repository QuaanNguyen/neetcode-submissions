class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        e.g for n = 2 we have:
        1.()()
        2.(())
        the size of output will always be 2n
        we can use recursion to print out all the possible permutations
        '''
        res: List[str] = []
        chars = ["(",")"] * n
        chars.sort()
        used = [False] * len(chars)

        def dfs(cur: str, open_used: int, close_used: int):
            if len(cur) == len(chars):
                res.append(cur)
                return
            if open_used < n:
                dfs(cur + "(", open_used + 1, close_used)
            if close_used < open_used:
                dfs(cur + ")", open_used, close_used +1)

        dfs("",0,0)
        return res

        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = []
        '''Constraints is to return itself if len==1'''
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            operand = ["+","-","/","*"]
            for i in tokens:
                if i in operand:
                    b = calc.pop()
                    a = calc.pop()
                    match(i):
                        case "+":
                            calc.append(a+b)
                        case "-":
                            calc.append(a-b)
                        case "/":
                            calc.append(int(a/b))
                        case "*":
                            calc.append(a*b)
                else:
                    calc.append(int(i))
        return calc[0]

                
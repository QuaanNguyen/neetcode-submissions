class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''Constraints is to return itself if len==1'''
        result = 0
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            operand = ["+","-","/","*"]
            calc = []
            for i in tokens:
                if i in operand:
                    b = calc.pop()
                    a = calc.pop()
                    match(i):
                        case "+":
                            c = a+b
                            calc.append(c)
                        case "-":
                            c = a-b
                            calc.append(c)
                        case "/":
                            c = int(a/b)
                            calc.append(c)
                        case "*":
                            c = a*b
                            calc.append(c)
                else:
                    calc.append(int(i))
                print(calc)
            result = calc[0]
        return result

                
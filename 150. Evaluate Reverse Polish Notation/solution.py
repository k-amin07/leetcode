from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if(i not in '+-*/'):
                stack.append(int(i))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                if(i == '+'):
                    stack.append(val1+val2)
                elif(i=='-'):
                    stack.append(val1-val2)
                elif(i=='*'):
                    stack.append(val1*val2)
                else:
                    stack.append(int(val1/val2))
        return stack[0]

solution = Solution()
solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
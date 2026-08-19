import operator
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack = []
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        for thing in tokens:
            if len(tokens) == 1:
                return int(thing)
            
            try:
                val = int(thing)
                stack.append(val)
                print("yo")
            except:
                value = operator_map[thing](stack[-2],  stack[-1])
                if value < 0 and value % 1 != 0:
                    print("buh")
                    value = math.ceil(value)
                if value > 0 and value % 1 != 0:
                    print("fah")
                    value = math.floor(value)
                stack.pop()
                stack.pop()
                stack.append(value)
                print(value)

        return int(value)




        
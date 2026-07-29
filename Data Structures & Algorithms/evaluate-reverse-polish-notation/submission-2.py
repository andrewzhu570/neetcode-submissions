class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for item in tokens:
            if item != "*" and item != "+" and item != "/" and item != "-":
                stk.append(item)
                continue
            num1 = int(stk.pop())
            num2 = int(stk.pop())
            if item == "*":
                stk.append(num1*num2)
            elif item == "/":
                stk.append(int(float(num2)/ num1))
            elif item == "+":
                stk.append(num2 + num1)
            else:
                stk.append(num2 - num1)
        return int(stk[0])
            
            
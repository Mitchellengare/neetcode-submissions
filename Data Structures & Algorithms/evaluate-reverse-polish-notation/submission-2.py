class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        char = {"+","-","*","/"}

        for i in tokens:
            if i not in char:
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
                if i == "+":
                    stack.append(l+r)
                elif i == "-":
                    stack.append(l-r)
                elif i == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))

        return stack[-1]
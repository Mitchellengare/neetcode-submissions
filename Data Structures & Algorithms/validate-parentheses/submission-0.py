class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)

            else:
                if not stack:
                    return False
            
                lastOpen = stack.pop()

                if char == "}" and lastOpen != "{":
                    return False
                if char == "]" and lastOpen != "[":
                    return False
                if char == ")" and lastOpen != "(":
                    return False

        if stack:
            return False

        return True  

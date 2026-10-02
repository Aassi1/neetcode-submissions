class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opening_bracket = "(", "{", "["
        closing_bracket = ")", "}", "]"

        matching = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for bracket in s:
            if bracket in opening_bracket:
                stack.append(bracket)
            else:
                if stack == []:
                    return False
                elif stack[-1] != matching[bracket]:
                    return False
                else:
                    stack.pop()
        return stack == []
                



        
        
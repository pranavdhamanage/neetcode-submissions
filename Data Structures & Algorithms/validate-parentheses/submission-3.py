class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for el in s:
            if el == '[' or el == '(' or el == '{':
                stack.append(el)
            else:
                if len(stack):
                    top = stack[len(stack) - 1]
                    if (el == ']' and top == '[') or (el == ')' and top == '(') or (el == '}' and top == '{'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            
        
        return len(stack) == 0
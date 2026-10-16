class Solution:
    def isValid(self, s: str) -> bool:

        # initialize the stack and the hashmap
        stack = []
        closeToOpen = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            # if encounter closing bracket, check whether the top of the stack
            # is the corresponding opening bracket
            if stack and c in closeToOpen:

                # return true and pop the opening bracket off the stack
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # if it is opening bracket, then append to the stack
            else:
                stack.append(c)
        
        # return true only when the stack is empty
        return True if not stack else False

class Solution(object):
    def isValid(self, s):
        valid = False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack += c
            elif c in [')']:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            elif c in ['}']:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    break
            elif c in [']']:
                if stack[-1] == '[':
                    queue.pop()
                else:
                    break

        if queue == []:
            valid = True

        return valid
    


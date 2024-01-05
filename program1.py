class Solution(object):
    def isValid(self, s):
        valid = False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                queue += c
            elif c in [')']:
                if queue[-1] == '(':
                    queue.pop()
                else:
                    break
            elif c in ['}']:
                if queue[-1] == '{':
                    queue.pop()
                else:
                    break
            elif c in [']']:
                if queue[-1] == '[':
                    queue.pop()
                else:
                    break

        if queue == []:
            valid = True

        return valid
    


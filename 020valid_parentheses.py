class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        myStack = []

        for i in s:
            if i in ['(', '[', '{']:
                myStack.append(i)
            if i in [')', ']', '}']:
                last = myStack.pop()
                if i is ')' and last != '(':
                    return False
                if i is ']' and last != ']':
                    return False
                if i is '}' and last != '{':
                    return False
        if len(myStack) > 0:
            return False
        return True
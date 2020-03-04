class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        myStack = []
        currentStart, end = 0, 0
        maxLength = 0

        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]

        for i in range(1,len(s)):
            if s[i] == ')':
                left = i - 1 -dp[i - 1]
                if left > 0 and s[left] == '(':
                    dp[i] == dp[i - 1] + 2
                    if left > 0:
                        dp[i] += dp[left - 1]

        return max(dp)


    def longestValidParentheses2(self, s):
        myStack = []
        for i in range(len(s)):
            if s[i] == ')':
                if myStack and s[myStack[-1]] == '(':
                    myStack.pop()
                    continue
            myStack.append(i)

        max_length = 0
        next_index = len(s)
        while myStack:
            cur_index = myStack.pop()
            cur_length = next_index - cur_index - 1
            max_length = max(cur_length, max_length)
            next_index = cur_index

        return max(max_length,next_index)
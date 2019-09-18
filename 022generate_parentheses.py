class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.add('', 0, 0, n)
        return self.res

    def add(self, s, left, right, n):
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.add(s + '(', left + 1, right, n)
        if right < left:
            self.add(s + ')', left, right + 1, n)

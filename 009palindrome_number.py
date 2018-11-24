class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        rev, y = 0, x
        while x > 0:
            rev = rev * 10 + x % 10
            x /= 10
        return rev == y



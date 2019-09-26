class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = (dividend < 0) == (divisor < 0)
        a, b, res = abs(dividend), abs(divisor), 0
        while a >= b:
            x = 0
            while a >= b << (x + 1):
                x += 1
            res += 1 << x
            a -= b << x
        return min(res if flag else -res, 2147483647)

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
            count, a = self._helper(a, b)
            res += count

        if flag == 0:
            res = -res

        return min(2 ** 31 - 1, max(-2 ** 31, res))

    def _helper(self, dividend, divisor):
        res, count = 0, 1
        while dividend >= divisor:
            dividend -= divisor
            divisor += divisor

            res += count
            count += count
        return res, dividend


a = Solution()
print(a.divide(20, 3))

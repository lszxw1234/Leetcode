class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx, step = 0, 1

        for x in s:
            res[idx] += x
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)
a = Solution()
print(a.convert('PAYPALISHIRING',3))


# def isInteresting(s):
#     offset = 0
#     i = 0
#     while i < len(s):
#         try:
#             offset = int(s[i])
#         except:
#             return False
#         i += offset + 1
#     if i == len(s):
#         return True
#     else:
#         return False
#
# print(isInteresting("2444gray6hunter"))
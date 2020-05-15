class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i,j = len(a),len(b)
        upper = 0
        res = ""
        while i > 0 and j > 0:
            curr = int(a[i - 1]) + int(b[j - 1]) + upper
            if curr >= 2:
                upper = 1
                res = str(curr%2) + res
            else:
                upper = 0
                res = str(curr) + res
            i -= 1
            j -= 1
        while i > 0:
            curr = int(a[i - 1]) + upper
            if curr >= 2:
                upper = 1
                res = str(curr%2) + res
            else:
                upper = 0
                res = str(curr) + res
            i -= 1
        while j > 0:
            curr = int(b[j - 1]) + upper
            if curr >= 2:
                upper = 1
                res = str(curr%2) + res
            else:
                upper = 0
                res = str(curr) + res
            j -= 1
        if upper == 1:
            res = "1" + res
        return res
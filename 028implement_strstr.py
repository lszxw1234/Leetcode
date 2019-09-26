class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack.__contains__(needle):
            return haystack.index(needle)
        else:
            return -1
        # or return haystack.find(needle)
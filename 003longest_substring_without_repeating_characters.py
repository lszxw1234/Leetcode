# Given a string, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """
        n = s.__len__()
        myset = set()
        l, start, end = 0,0,0
        while(start < n and  end < n):
            if s[end] not in myset:
                myset.add(s[end])
                end += 1
                l = max(l, end-start)
            else:
                myset.remove(s[start])
                start += 1
        return l
a = Solution()
print(a.lengthOfLongestSubstring('dvdf'))


print(a.lengthOfLongestSubstring('asdfgds'))
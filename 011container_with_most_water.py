class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxarea = 0
        while(i < j):
            tmparea = min(height[i],height[j]) * (j - i)
            maxarea = max(maxarea,tmparea)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxarea


a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))

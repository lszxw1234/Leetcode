class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n, 0, -1):
            if nums[i - 1] == val:
                nums.remove(val)

        return len(nums)
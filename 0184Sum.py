class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif tmp > target:
                        r -= 1
                    else:
                        l += 1
            return res
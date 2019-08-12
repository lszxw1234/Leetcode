class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n, res = len(nums), -18888888
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i+1,n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    r -= 1
                    if abs(target - res) > abs(target - tmp):
                        res = tmp
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    l += 1
                    if abs(target - res) > abs(target-tmp):
                        res = tmp
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

a = Solution()
print(a.threeSumClosest([-1,2,1,-4],1))

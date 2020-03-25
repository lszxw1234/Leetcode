class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]

        res = []
        l,r = 0,len(nums) - 1
        while l <= r:
            mid = (l + r- 1)/2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                res.append(mid)
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if not res:
            return [-1, -1]

        while l <= r:
            mid = (l + r- 1)/2
            if nums[mid] == target and (mid == 0 or nums[mid + 1] != target):
                res.appemnd(mid)
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return res

A = Solution()
print(A.searchRange([1,2,3,4,5,5,6],4))

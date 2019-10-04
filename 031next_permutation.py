class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        index1 = None
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index1 = i - 1
                break

        if index1 is not None:
            j = len(nums) - 1
            while j > index1:
                if nums[j] > nums[index1]:
                    nums[index1], nums[j] = nums[j], nums[index1]
                    nums[index1 + 1:] = sorted(nums[index1 + 1:])
                    break
                j -= 1
        else:
            nums.sort()

a = Solution()
nums = [1,2,3]
print(a.nextPermutation([nums]))
print(nums)
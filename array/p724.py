class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = 0
        b = sum(nums)
        for i in range(len(nums)):
            b -= nums[i]
            if a == b:
                return i
            a += nums[i]
        return -1

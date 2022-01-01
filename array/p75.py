class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        a = 0
        b = len(nums)-1
        
        while i <= b:
            if nums[i] == 0:
                nums[i], nums[a] = nums[a], nums[i]
                a += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else:
                i += 1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        L = 0
        R = len(nums)-1
        pivot = 0
        while L < R:
            pivot = (L+R)//2

            if nums[pivot] < nums[pivot+1]:
                L = pivot + 1
            else:
                R = pivot
        return L
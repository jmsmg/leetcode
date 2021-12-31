class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        
        while L <= R:
            pivot = (L+R)//2
            if nums[pivot] < target:
                L = pivot+1
            elif target < nums[pivot]:
                R = pivot-1
            else:
                return pivot
        return -1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1)-1
        a = m-1
        b = n-1
        
        while (0 <= a and 0 <= b):
            if nums1[a] < nums2[b]:
                nums1[i] = nums2[b]
                b -= 1
            else:
                nums1[i] = nums1[a]
                a -= 1
            i -= 1
        while 0 <= b:
            nums1[i] = nums2[b]
            i -= 1
            b -= 1
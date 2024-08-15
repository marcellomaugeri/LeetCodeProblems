class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        to_order = n+m-1
        i = m-1
        j = n-1
        # The trick consists in starting from the end of the array and moving the biggest element to the end of the array, the complexity is O(n+m)
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[to_order] = nums1[i]
                i-=1
            else:
                nums1[to_order] = nums2[j]
                j-=1
            to_order-=1
        while j>=0:
            nums1[to_order] = nums2[j]
            to_order-=1
            j-=1
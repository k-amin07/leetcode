class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        merged_array = [0]*(n1 + n2)
        i = 0
        j = 0
        k = 0
        while (i < n1 and j < n2):
            if (nums1[i] < nums2[j]):
                merged_array[k] = nums1[i]
                k = k + 1
                i = i + 1
            else:
                merged_array[k] = nums2[j]
                k = k + 1
                j = j + 1
        while (i < n1):
            merged_array[k] = nums1[i]
            k = k + 1
            i = i + 1
        while (j < n2):
            merged_array[k] = nums2[j]
            k = k + 1
            j = j + 1
        if ((n1+n2) % 2):
            return merged_array[(n1+n2)//2]
        else:
            return (merged_array[(n1+n2)//2] + merged_array[(n1+n2-1)//2])/2



solution = Solution()

solution.findMedianSortedArrays([1,2],[3,4])
# Q4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        else:
            return nums[len(nums) // 2]
        
if __name__ == "__main__":
    print("Q4. Median of Two Sorted Arrays")
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [0, 0]
    nums2 = [0, 0]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = []
    nums2 = [1]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    nums1 = [2]
    nums2 = []
    print(Solution().findMedianSortedArrays(nums1, nums2))
    print("End of Q4. Median of Two Sorted Arrays")

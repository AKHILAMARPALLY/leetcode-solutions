class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays.
        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        """
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            # Partition nums1
            cut1 = (low + high) // 2
            # Partition nums2 such that left side has equal elements as right side
            cut2 = (m + n + 1) // 2 - cut1
            
            # Handle edge cases for left and right values
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]
            right2 = float('inf') if cut2 == n else nums2[cut2]
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                # If total length is odd
                else:
                    return max(left1, left2)
            
            # Move the partition
            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        
        return -1  # Should never reach here for valid inputs


# Test cases
def test_solution():
    sol = Solution()
    
    # Example 1
    nums1 = [1, 3]
    nums2 = [2]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(f"Example 1: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: 2.0\n")
    
    # Example 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(f"Example 2: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: 2.5\n")
    
    # Additional test case
    nums1 = []
    nums2 = [1]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(f"Edge case: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: 1.0\n")
    
    # Additional test case
    nums1 = [0, 0]
    nums2 = [0, 0]
    result = sol.findMedianSortedArrays(nums1, nums2)
    print(f"Edge case: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result}")
    print(f"Expected: 0.0\n")


if __name__ == "__main__":
    test_solution()
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)  # Convert nums1 to a set for fast lookups
        result = set()     # Initialize an empty set to store the intersection
        for num in nums2:  # Iterate over each element in nums2
            if num in seen:  # Check if the current element is in the set 'seen'
                result.add(num)  # Add to result if the number is in seen
        return list(result)
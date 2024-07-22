class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)  # Convert nums1 to a set for fast lookups
        for n in list(seen):  # Iterate over a copy of the set to avoid modification during iteration
            if n not in nums2:
                seen.remove(n)
        return list(seen)  # Convert the set to a list before returning

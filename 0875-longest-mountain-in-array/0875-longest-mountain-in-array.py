'''
iterate through the array to find the peak. Once found the peak, expand both left and right to find the length of that mountain
condition to expand left and right:
keep moving left if arr[left] < arr[left + 1]
moveing righ if arr[right] < ar[right + 1]

no valid peak: return 0
arr.len < 3 -> retủn 0 since we need 3 element
'''
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        maxLen = 0
        for i in range(1, len(arr)-1):
            #find peak
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                #expand left right
                left = i-1
                right = i+1
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                while right < (len(arr)-1) and arr[right] > arr[right + 1]:
                    right += 1
                maxLen = max(right - left+1, maxLen)
        return maxLen



        
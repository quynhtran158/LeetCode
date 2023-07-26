class Solution {
    public boolean containsDuplicate(int[] nums) {
    Arrays.sort(nums); //do cái code này nó bắt cặp lần lươt. kiểu 0-1, 1-2. Mà trong array 1,2,3,1 thì nó kh pair đc 1st lást num --> sort để các số nhỏ lặp đứng gần nhau thì dễ so hơn
    for (int i = 0; i < nums.length - 1; ++i) {
        if (nums[i] == nums[i + 1]) return true;
    }
    return false;
}
}
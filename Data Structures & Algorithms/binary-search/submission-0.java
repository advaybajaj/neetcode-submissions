class Solution {
    public int search(int[] nums, int target) {
        int minIndex=0, maxIndex=nums.length-1;
        while (minIndex<=maxIndex) {
            int midIndex = (minIndex + maxIndex) / 2;
            if(nums[midIndex] == target) {
                return midIndex;
            } else if (nums[midIndex] < target) {
                minIndex = midIndex+1;
            } else {
                maxIndex = midIndex-1;
            }
        }
        return -1;
    }
}

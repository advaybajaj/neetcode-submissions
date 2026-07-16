class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int j=0, k=0, target=0;
        List<List<Integer>> listOfLists = new LinkedList<>();
        for(int i=0; i<nums.length; i++) {
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            j=i+1;
            k=nums.length-1;
            target=0-nums[i];
            while(j<k) {
                if(nums[j]+nums[k]==target) {
                    listOfLists.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    while(j<k && nums[j]==nums[j+1]){
                        j++;
                    } 
                    while(j<k && nums[k]==nums[k-1]){
                        k--;
                    }
                    j++;
                    k--;
                } else if (nums[j]+nums[k]>target) {
                    k--;
                } else if (nums[j]+nums[k]<target) {
                    j++;
                }
            }
        }
        return listOfLists;
    }
}

class Solution {
    public int maxArea(int[] heights) {
        int l=0, r=heights.length-1, area=0, height=0, maxArea=0;
        while(l<r) {
            if(heights[l]<heights[r]) {
                height = heights[l];
            } else {
                height = heights[r];
            }
            area = (r-l) * height;
            if(area > maxArea) {
                maxArea = area;
            }

            if(heights[l]<heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
}

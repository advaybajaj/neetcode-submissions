class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int numRows = matrix.length;
        int numCols = matrix[0].length;
        int l=0, r=(numRows*numCols)-1;
        while (l<=r) {
            int mid = (l+r)/2;
            int row = mid / numCols;
            int col = mid % numCols;
            if(matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return false;
    }
}

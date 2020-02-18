class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums == null) {
            return 0;
        } else if (nums.length == 1) {
            return 1;
        }
        int noDups = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i - 1] < nums[i]) {
                nums[noDups] = nums[i];
                noDups++;
            }
        }
        return noDups;
    }
}

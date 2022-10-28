public class myans {
    public int pivotIndex(int[] nums) {
        int sumOfList = 0;
        for (int i = 0; i < nums.length; i++) {
            sumOfList = sumOfList + nums[i];
        }
        int leftsum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (leftsum == (sumOfList - leftsum - nums[i]))
                return i;
            leftsum = leftsum + nums[i];
        }
        return -1;
    }
}

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int idx = 0;
        int count = 1;
        for (int i = 1; i < nums.size(); ++i)
        {
            nums[idx] == nums[i] ? ++count : --count;
            if (count == 0)
            {
                idx = i;
                count = 1;
            }
        }
        return nums[idx];
    }
};
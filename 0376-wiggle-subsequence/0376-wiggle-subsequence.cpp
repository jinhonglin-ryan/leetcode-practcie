class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        if (nums.size() <= 2) return nums.size();
        int res = 2;
        for (int i = 1; i + 1 < nums.size(); i ++ ) {
            int a = nums[i - 1], b = nums[i], c = nums[i + 1];
            if (b > a && b > c || b < a && b < c) res ++ ;
        }
        return res;
    }
};


/*
Question Link
    https://leetcode.com/problems/wiggle-sort-ii/
*/
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        if (nums.size() <= 1) return;
        vector<int> cnt = vector<int>(sizeof(nums)/sizeof(nums[0])+1, 0);
        
        int max_val = -1;
        for (int i: nums) {
            cnt[i]++;
            max_val = max(i, max_val);
        }
        
        int val = max_val;
        
        for (int i = 1; i < nums.size(); i+=2) {
            while (cnt[val] == 0) val--;
            nums[i] = val;
            cnt[val]--;
        }
        
        for (int i = 0; i < nums.size(); i+=2) {
            while (cnt[val] == 0) val--;
            nums[i] = val;
            cnt[val]--;
        }
        
    }
};
/*
Question Link
    https://leetcode.com/problems/minimum-absolute-sum-difference/
*/
class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        int absSum=0;
        int size=nums1.size();
        vector<int>diff(size);
        int m=1e9+7;
        for(int i=0;i<size;i++){
            diff[i]=abs(nums1[i]-nums2[i]);
            absSum=(absSum+abs(nums1[i]-nums2[i]))%m;
        }
        sort (nums1.begin(),nums1.end()); 
        vector<int>arr(size);
        for(int i=0;i<size;i++){
            int lower_bound_index=lower_bound(nums1.begin(),nums1.end(),nums2[i])-nums1.begin();
            if(lower_bound_index!=0 && lower_bound_index!=size){             
                arr[i]=min(abs(nums2[i]-nums1[lower_bound_index]),abs(nums2[i]-nums1[lower_bound_index-1]));
            }else if(lower_bound_index==0){
                arr[i]=abs(nums2[i]-nums1[0]);
            }else if(lower_bound_index==size){
                arr[i]=abs(nums2[i]-nums1[lower_bound_index-1]);
            }
        }
        int bestDiff=0;
        for(int i=0;i<size;i++){
            bestDiff=max(bestDiff,diff[i]-arr[i]);
        }
        return ((absSum-bestDiff)+m)%m;
    }
};
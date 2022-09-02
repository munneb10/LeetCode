/*
Question Link
        https://leetcode.com/problems/two-sum/
*/
#include <limits>
class Solution {
public:
    int no1;
    int no2;
    int max=std::numeric_limits<int>::max();
    void MergeSortedIntervals(vector<int>& v, int s, int m, int e) {
	vector<int> temp;

	int i, j;
	i = s;
	j = m + 1;

	while (i <= m && j <= e) {

		if (v[i] <= v[j]) {
			temp.push_back(v[i]);
			++i;
		}
		else {
			temp.push_back(v[j]);
			++j;
		}

	}

	while (i <= m) {
		temp.push_back(v[i]);
		++i;
	}

	while (j <= e) {
		temp.push_back(v[j]);
		++j;
	}

	for (int i = s; i <= e; ++i)
		v[i] = temp[i - s];

}
void MergeSort(vector<int>& v, int s, int e) {
	if (s < e) {
		int m = (s + e) / 2;
		MergeSort(v, s, m);
		MergeSort(v, m + 1, e);
		MergeSortedIntervals(v, s, m, e);
	}
}
    vector<int> findInd(vector<int>& nums){
        vector<int> a=vector<int>(2);
        for(int i=0;i<nums.size();i++){
            if(no1== max & no2== max){
                break;
            }
            if(nums[i]==no1 & no1!=max){
                a[0]=i;
                no1= max;
            }else if(nums[i]==no2 & no2!=max){
                a[1]=i;
                no2= max;
            }
        }
        return a;
    }
    vector<int> twoSum(vector<int>& nums, int target) {
        int size=nums.size();
        vector<int> temp=nums;
        MergeSort(temp,0,size-1);
        no1=0;
        no2=nums.size()-1;
        while(temp[no1]+temp[no2]!=target){
            if(temp[no1]+temp[no2]>target){
                no2--;
            }else{
                no1++;
            }
        }
        no1=temp[no1];
        no2=temp[no2];
        vector<int> indexes=findInd(nums);
        return indexes;
    }
};







class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = nums1.size() - 1;
        
        while(i >= 0) {
            nums1[j--] = nums1[i--];
        }
        
        i = j + 1;
        j = 0;
        m = 0;
        while(i < nums1.size() && j < n){
            if(nums1[i] < nums2[j]){
                nums1[m++] = nums1[i++];
            } else {
                nums1[m++] = nums2[j++];
            }
        }
        
        while(i < nums1.size()){
            nums1[m++] = nums1[i++];
        }
        
        while(j < n){
            nums1[m++] = nums2[j++];
        }
    }
};

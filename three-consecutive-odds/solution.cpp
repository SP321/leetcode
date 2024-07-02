class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        for(int i=1;i<arr.size()-1;i++){
            if(arr[i]%2 and arr[i-1]%2 and arr[i+1]%2)
                return 1;
        }
        return 0;
    }
};
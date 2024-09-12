class Solution {
public:
    bool isSelfCrossing(vector<int>& arr) {
        for(int i = 3; i < arr.size(); i ++){
            if(i >= 3 && arr[i] >= arr[i - 2] 
            and arr[i - 1] <= arr[i - 3])
                return true;
            
            if(i >= 4 && arr[i - 1] == arr[i - 3] 
            and arr[i] + arr[i - 4] >= arr[i - 2]) 
                return true;
            
            if(i >= 5 && arr[i - 2] >= arr[i - 4] 
            and arr[i - 5] + arr[i - 1] >= arr[i - 3] 
            and arr[i - 1] <= arr[i - 3] 
            and arr[i - 4] + arr[i] >= arr[i - 2]) 
                return true;
        }
        return false;  
    }
};
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int n=arr.size();
        int x=-1;
        for(int i=n-1;i>=0;i--){
            int y=max(x,arr[i]);
            arr[i]=x;
            x=y;
        }
        return arr;
    }
};
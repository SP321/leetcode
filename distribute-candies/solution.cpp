class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        sort(candyType.begin(),candyType.end());
        int diff=1;
        for(int i=1;i<candyType.size();i++){
            if(diff==candyType.size()/2)
                return diff;
            if(candyType[i]>candyType[i-1])
                diff++;
        }
        return diff;
    }
};
class Solution {
public:
    Solution(){
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
    }
    int minSwaps(string s) {
        int c=0;
        int changes=0;
        for(auto x:s){
            if(x==']')
                c+=1;
            else
                c-=1;
            changes=max(changes,c);
        }
        return (changes+1)/2;
    }
};
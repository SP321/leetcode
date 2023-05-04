class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>>xs;
        for(auto &i:buildings){
            int x1=i[0];
            int x2=i[1];
            int h=i[2];
            xs.push_back({x1, -h});
            xs.push_back({x2, h});
        }
        sort(xs.begin(),xs.end());
        set<int>s;
        s.insert(0);
        vector<vector<int>>ans;
        int prev = 0;
        map<int,int>sc;
        for(auto&i:xs){
            if(i[1]<0){
                sc[i[1]]++;
                s.insert(i[1]);
            }
            else{
                sc[-i[1]]--;
                if(sc[-i[1]]==0)
                    s.erase(-i[1]);
            }
            int cur=-*s.begin();
            cout<<i[1]<<" "<<s.size()<<endl;
            if(cur!=prev)
                ans.push_back({i[0],cur});
            prev=cur;
        }
        return ans;
    }
};
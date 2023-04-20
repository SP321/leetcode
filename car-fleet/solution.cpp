class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<int>id;
        int n=position.size();
        for(int i=0;i<n;i++)
            id.push_back(i);
        sort(id.begin(),id.end(),[&position](int a,int b){return position[a]>position[b];});
        stack<float>x;
        int pos=position[id[0]];
        int sped=speed[id[0]];
        float maxt=(float)(target-pos)/sped;
        int ans=1;
        for(int i=1;i<n;i++){
            int pos=position[id[i]];
            int sped=speed[id[i]];
            float t=(float)(target-pos)/sped;
            if(t>maxt){
                maxt=t;
                ans++;
            }
        }
        return ans;
    }
};
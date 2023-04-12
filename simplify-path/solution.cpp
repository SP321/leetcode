class Solution {
public:
    string simplifyPath(string path) {
        vector<string>a;
        int j=0;
        path=path+"/";
        for(int i=0;i<path.size();i++){
            if(path[i]=='/'){
                if(i!=0){
                    string x=path.substr(j+1,i-j-1);
                    if(x.size()){
                        if(x==".."){
                            if(a.size())
                                a.pop_back();
                        }
                        else if(x!=".")
                            a.push_back(x);
                    }
                }
                j=i;
            }
        }
        string ans="";
        for(string &x:a)
            ans=ans+"/"+x;
        if(!ans.size())
            return "/";
        return ans;
    }
};
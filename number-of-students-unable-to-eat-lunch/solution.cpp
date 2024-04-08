class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        vector<int>c(2);
        for(int &x:students)
            c[x]+=1;
        for(int &x:sandwiches){
            if(c[x]>0)
                c[x]-=1;
            else
                return c[0]+c[1];
        }
        return 0;
    }
};
class Solution {
public:
    vector<int> constructRectangle(int area) {
        int factor=1,i=2;
        while(i*i<=area){
            if(area%i==0)
                factor=i;
            i+=1;
        }
        return {area/factor,factor};
    }
};
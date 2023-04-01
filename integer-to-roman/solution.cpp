class Solution {
public:
    string intToRoman(int num) {
        int nums[]={1,4,5,9,10,40,50,90,100,400,500,900,1000};
        string s[]={"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        int i=sizeof(nums)/sizeof(nums[0]);
        string ans="";
            i--;
        while(num>0){
            int d=num/nums[i];
            num=num%nums[i];
            for(int j=0;j<d;j++)
                ans+=s[i];
            i--;
        }
        return ans;
    }
};
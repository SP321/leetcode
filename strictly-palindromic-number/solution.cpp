class Solution {
public:
    int toBase(int n,int b){
        long long ans=0;
        while(n>0){
            ans+=n%b;
            ans*=10;
            n/=b;
        }
        return ans;
    }
    bool isPalindrome(long long n){
        long long reverse=0;
        long long n2=n;
        while(n>0){
            reverse=(10*reverse)+n%10;
            n/=10;
        }
        return n2==reverse;
    }
    bool isStrictlyPalindromic(int n) {
        bool ans=1;
        for(int i=2;i<n-1;i++){
            ans= ans && isPalindrome(toBase(n,i));
        }
        return ans;
    }
};
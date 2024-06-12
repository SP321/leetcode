class ATM {
public:
    vector<int>a={20,50,100,200,500};
    vector<int>c;
    ATM() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        c=vector<int>(5);
    }
    
    void deposit(vector<int> banknotesCount) {
        for(int i=0;i<5;i++){
            c[i]+=banknotesCount[i];
        }
    }
    
    vector<int> withdraw(int amount) {
        vector<int>cur(5);
        for(int i=4;i>=0;i-=1){
            int x=min(c[i],amount/a[i]);
            cur[i]+=x;
            amount-=a[i]*x;
        }
        if(amount!=0)
            return {-1};
        for(int i=0;i<5;i++){
            c[i]-=cur[i];
        }
        return cur;
    }
};

/**
 * Your ATM object will be instantiated and called as such:
 * ATM* obj = new ATM();
 * obj->deposit(banknotesCount);
 * vector<int> param_2 = obj->withdraw(amount);
 */
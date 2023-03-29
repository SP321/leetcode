#include <bits/stdc++.h>
using namespace std;
 
 class Solution {
public:
    int minPartitions(string n) {
        char ans='0';
        for(int i=0;i<size(n);i++)
            ans=max(ans,n[i]);
        return ans-'0';
    }
};
class Solution {
public:
    string smallestSubsequence(string s) {
        stack<char>st;
        vector<int>lastindex(26,0);
        vector<bool>seen(26,false);
        for(int i = 0 ;i<s.size();i++)
        {
            lastindex[s[i] - 'a'] = i; 
        }
        for(int i = 0 ;i<s.size();i++)
        {
            int curr = s[i] - 'a'; 
            if(seen[curr])
            {
                continue;
            }
            while(st.size() > 0 && st.top() > s[i] && i < lastindex[st.top()-'a'])
            {
                seen[st.top() - 'a'] = false;
                st.pop();
            }
            st.push(s[i]);
            seen[curr] = true;  
        }
        string res= "";
        while(st.size() > 0)
        {
            res += st.top();
            st.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
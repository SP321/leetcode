//https://cp-algorithms.com/string/aho_corasick.html
const int K = 26;

struct Vertex {
    int next[K];
    int p = -1;
    char pch;
    int link = -1;
    int go[K];
    int ln=0;
    Vertex(int p=-1, char ch='$', int ln=0) : p(p), pch(ch), ln(ln) {
        fill(begin(next), end(next), -1);
        fill(begin(go), end(go), -1);
    }
};

vector<Vertex> t(1);

void add_string(string const& s) {
    int v = 0;
    for (char ch : s) {
        int c = ch - 'a';
        if (t[v].next[c] == -1) {
            t[v].next[c] = t.size();
            t.emplace_back(v, ch, t[v].ln+1 );
        }
        v = t[v].next[c];
    }
}

int go(int v, char ch);

int get_link(int v) {
    if (t[v].link == -1) {
        if (v == 0 || t[v].p == 0)
            t[v].link = 0;
        else
            t[v].link = go(get_link(t[v].p), t[v].pch);
    }
    return t[v].link;
}

int go(int v, char ch) {
    int c = ch - 'a';
    if (t[v].go[c] == -1) {
        if (t[v].next[c] != -1)
            t[v].go[c] = t[v].next[c];
        else
            t[v].go[c] = v == 0 ? 0 : go(get_link(v), ch);
    }
    return t[v].go[c];
} 

class Solution {
public:
    int minValidStrings(vector<string>& words, const string& target) {
        t.clear(); t.shrink_to_fit(); t = vector<Vertex>(1);
        for(auto &x:words)
            add_string(x);
        int n = target.size();
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;
        int cur=0;
        for (int i=0;i<target.size();i++){
            char ch=target[i];
            cur=go(cur,ch);
            if(t[cur].ln>0) 
                dp[i + 1] = min(dp[i + 1], dp[i + 1 - t[cur].ln] + 1);
        }

        return dp[n] != 1e9 ? dp[n] : -1;
    }
};
class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        k +='a';
        int n = s.size();
        auto find=[&] (int i, char c){
            while ((i >= 1 && c == s[i - 1]) || (i >= 2 && c == s[i - 2]))
                c+=1;
            return c;
        };
        for (int i = n - 1; i >= 0; --i) {
            char c = find(i, s[i] + 1);
            if (c < k) {
                s[i] = c;
                for (int j=i+1; j < n; j++) {
                    s[j] = find(j,'a');
                }
                return s;
            }
        }
        return "";
    }
};
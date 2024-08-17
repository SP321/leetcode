class Solution {
public:
    bool isVowel(char c) {
        c = tolower(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
    string reverseVowels(string s) {
        int i = 0;
        int j = s.length()-1;

        while(i<j){
            if(isVowel(s[i]) and isVowel(s[j])){
                swap(s[i++],s[j--]);
            }
            else if(!isVowel(s[i])){
                i++;
            }
            else j--;
        }
        return s;
    }
};
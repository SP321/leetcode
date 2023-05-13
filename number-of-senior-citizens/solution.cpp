class Solution {
public:
    int countSeniors(std::vector<std::string>& details) {
        int count = 0;
        for (auto & detail : details) {
            int age = stoi(detail.substr(detail.length() - 4, 2));
            if (age > 60) {
                count++;
            }
        }
        
        return count;
    }
};
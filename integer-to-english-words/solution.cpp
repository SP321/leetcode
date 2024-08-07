class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) {
            return "Zero";
        }

        vector<string> lessThan20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        vector<string> tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        vector<string> thousands = {"", "Thousand", "Million", "Billion"};

        string result;
        int i = 0;

        while (num > 0) {
            int triplet = num % 1000;
            if (triplet != 0) {
                result = helper(triplet, lessThan20, tens) + thousands[i] + " " + result;
            }
            num /= 1000;
            i++;
        }

        while (!result.empty() && result.back() == ' ') {
            result.pop_back();
        }

        return result;
    }

    string helper(int num, const vector<string>& lessThan20, const vector<string>& tens) {
        if (num == 0) {
            return "";
        } else if (num < 20) {
            return lessThan20[num] + " ";
        } else if (num < 100) {
            return tens[num / 10] + " " + helper(num % 10, lessThan20, tens);
        } else {
            return lessThan20[num / 100] + " Hundred " + helper(num % 100, lessThan20, tens);
        }
    }
};
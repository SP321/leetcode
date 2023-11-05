class Solution {
public:
    int getWinner(vector<int>& arr, int k) {
        int current_winner = arr[0];
        int win_count = 0;
        
        for (int i = 1; i < arr.size(); ++i) {
            if (current_winner > arr[i]) {
                win_count++;
            } else {
                current_winner = arr[i];
                win_count = 1;
            }

            if (win_count == k) {
                return current_winner;
            }
        }

        return current_winner;
    }
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 auto speedUP = [](){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();

class Solution {
public:
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> grid(m, vector<int>(n, -1));

        int x1 = 0, y1 = 0;
        int x2 = m - 1, y2 = n - 1;

        while (head) {
            for (int j = y1; j <= y2 && head; ++j) {
                if(head){
                    grid[x1][j] = head->val;
                    head = head->next;
                }
            }
            x1++;

            for (int i = x1; i <= x2 && head; ++i) {
                if(head){
                    grid[i][y2] = head->val;
                    head = head->next;
                }
            }
            y2--;

            for (int j = y2; j >= y1 && head; --j) {
                if(head){
                    grid[x2][j] = head->val;
                    head = head->next;
                }
            }
            x2--;

            for (int i = x2; i >= x1 && head; --i) {
                if(head){
                    grid[i][y1] = head->val;
                    head = head->next;
                }
            }
            y1++;
        }
        return grid;
    }
};
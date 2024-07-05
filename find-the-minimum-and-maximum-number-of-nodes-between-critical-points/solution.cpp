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
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ios_base::sync_with_stdio(false);
        ListNode *node = head;
        ListNode *prev = nullptr;
        int pos = 1;
        int first = -1;
        int last = -1;
        int mi = INT_MAX;

        while (node) {
            if (prev != nullptr && node->next != nullptr) {
                if ((prev->val < node->val && node->val > node->next->val) ||
                 (prev->val > node->val && node->val < node->next->val)) {
                    if (first == -1) {
                        first = pos;
                    } else {
                        mi = min(mi, pos - last);
                    }
                    last = pos;
                }
            }
            prev = node;
            node = node->next;
            pos++;
        }
        if (mi == INT_MAX) {
            return {-1, -1};
        }
        return {mi, last - first};
    }
};
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
    ListNode* doubleIt(ListNode* head) {
        function<int(ListNode*)> helper = [&](ListNode* node) -> int {
            if (!node) return 0;
            int carry = helper(node->next);
            int val2 = node->val * 2 + carry;
            node->val = val2 % 10;
            return val2 / 10;
        };
        int carry = helper(head);
        if (carry > 0) {
            return new ListNode(carry, head);
        }
        return head;
    }
};
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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr = head;
        while (curr && curr->next) {
            int gcd_val = __gcd(curr->val, curr->next->val);
            ListNode* new_node = new ListNode(gcd_val);
            new_node->next = curr->next;
            curr->next = new_node;
            curr = curr->next->next;
        }
        return head;
    }
};
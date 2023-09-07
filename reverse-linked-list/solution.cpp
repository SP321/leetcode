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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = 0;
        ListNode* cur = head;

        while (cur != 0) {
            ListNode* t = cur->next;
            cur->next = prev;
            prev = cur;
            cur = t;
        }
        
        return prev;
    }
};
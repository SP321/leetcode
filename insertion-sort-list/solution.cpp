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
    ListNode* insertionSortList(ListNode* head) {
        if (!head->next) return head;
        ListNode dummy(0);
        ListNode* prev = &dummy;
        while (head) {
            ListNode* next = head->next;
            if (!prev->next || prev->next->val > head->val)
                prev = &dummy;
            while (prev->next && prev->next->val < head->val)
                prev = prev->next;
            head->next = prev->next;
            prev->next = head;
            head = next;
        }
        return dummy.next;
    }
};
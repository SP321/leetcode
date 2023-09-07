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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* first = &dummy;
        ListNode* second = &dummy;
        n+=1;
        while(n--)
            first = first->next;

        while (first) {
            first = first->next;
            second = second->next;
        }

        ListNode* node_to_delete = second->next;
        second->next = second->next->next;
        delete node_to_delete;

        return dummy.next;
    }
};
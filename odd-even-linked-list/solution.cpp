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
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return nullptr;

       ListNode* a = new ListNode(0);
       ListNode* b = new ListNode(0);
       ListNode* c = a;
       ListNode* d = b;
       ListNode* cur = head;
       bool fl = true;

       while (cur) {
           if (fl) {
               c->next = cur;
               c = c->next;
           }
           else {
               d->next = cur;
               d = d->next;
           }
           cur = cur->next;
           fl = !fl;
       }

       c->next = b->next;
       d->next = nullptr;

       return a->next;
    }
};
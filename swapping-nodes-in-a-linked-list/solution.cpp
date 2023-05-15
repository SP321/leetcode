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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* j=head, * y=head, *x;
        while(--k)
            j=j->next;
        x=j;
        while(j->next){
            y=y->next;
            j=j->next;
        }
        swap(x->val,y->val);
        return head;
    }
};
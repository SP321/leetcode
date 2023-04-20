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
    ListNode* swapPairs(ListNode* head) {

        ListNode* cur1=head;
        ListNode* cur2=nullptr;
        if(!cur1)
            return cur1;
        ListNode* newhead=head;
        if(cur1->next)
            newhead=cur1->next;
        ListNode* prev2=nullptr;
        while(cur1 && cur1->next){
            cur2=cur1->next;
            cur1->next=cur2->next;
            cur2->next=cur1;
            if(prev2)
                prev2->next=cur2;
            prev2=cur1;
            cur1=cur1->next;
        }
        return newhead;
    }
};
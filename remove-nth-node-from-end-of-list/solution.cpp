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
        ListNode* a2=head;
        ListNode* a3=head;
        n--;
        while(n--)
            a3=a3->next;
        ListNode* a1=nullptr;
        while(a3->next!=nullptr){
            a1=a2;
            a2=a2->next;
            a3=a3->next;
        }
        if(!a1)
            return head->next;
        a1->next=a2->next;
        return head;
    }
};
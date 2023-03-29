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

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head=nullptr;
        ListNode* current=nullptr;
        int ans=0;
        int rem=0;
        while (l1!=nullptr or l2!=nullptr){
            int n1=0,n2=0;
            if(l1!=nullptr){
                n1=l1->val;
                l1=l1->next;
            }
            if(l2!=nullptr){
                n2=l2->val;
                l2=l2->next;
            }
            int val=n1+n2+rem;
            rem=val/10;
            ListNode* x=new ListNode((val%10));
            if(head==nullptr)
                head=x;
            if(current!=nullptr){
                cout<<current;
                current->next=x;
            }
            current=x;
        }
        if(rem!=0)
            current->next=new ListNode(rem);
        return head;
    }
};
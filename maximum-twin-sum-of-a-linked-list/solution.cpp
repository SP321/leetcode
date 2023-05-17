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
    int pairSum(ListNode* head) {
        ListNode *lefthead=nullptr,*righthead=head,*x=head;
        while (x && x->next){
            x=x->next->next;
            ListNode* tmp=righthead->next;
            righthead->next=lefthead;
            lefthead=righthead;
            righthead=tmp;
        }
        int ans=0;
        while(lefthead){
            ans=max(ans,lefthead->val+righthead->val);
            lefthead=lefthead->next;
            righthead=righthead->next;
        }
        return ans;
    }
};
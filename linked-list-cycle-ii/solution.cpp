/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        map<ListNode*,int>d;
        while(head){
            if(d[head])
                return head;
            d[head]=1;
            head=head->next;
        }
        return 0;
    }
};
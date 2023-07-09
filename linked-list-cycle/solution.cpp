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
    bool hasCycle(ListNode *head) {
        map<ListNode*,int>d;
        while(head){
            if(d[head])
                return 1;
            d[head]=1;
            head=head->next;
        }
        return 0;
    }
};
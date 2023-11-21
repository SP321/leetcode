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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* prev=NULL;
        ListNode* node=head;
        while(node){
            if(prev && node->val==prev->val)
                prev->next=node->next;
            else
                prev=node;
            node=node->next;
        }
        return head;
    }
};
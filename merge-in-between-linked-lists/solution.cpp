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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *l=list1,*r=list1;
        for(int i=0;i<a-1;i++)
            l=l->next;
        for(int i=0;i<b;i++)
            r=r->next;
        l->next=list2;
        while(l->next)
            l=l->next;
        l->next=r->next;
        return list1;
    }
};
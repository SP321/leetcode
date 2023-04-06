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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* head=nullptr;
        ListNode* a;
        ListNode* tail=nullptr;
        if(list1==nullptr)
            return list2;
        if(list2==nullptr)
            return list1;
        while(list1!=nullptr && list2 !=nullptr){
            while(list1!=nullptr && list1->val<=list2->val){
                a=list1;
                if(head==nullptr)
                    head=a;
                else
                    tail->next=a;
                tail=a;
                cout<<a->val<<endl;
                list1=list1->next;
            }
            if(list1==nullptr || list2 ==nullptr)
                break;
            while(list2 !=nullptr && list1->val>=list2->val){
                a=list2;
                if(head==nullptr)
                    head=a;
                else
                    tail->next=a;
                tail=a;
                cout<<a->val<<endl;
                list2=list2->next;
            }
        }
        if(list1!=nullptr)
            tail->next=list1;
        else if (list2!=nullptr)
            tail->next=list2;
        return head;
    }
};
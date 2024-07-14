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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        unordered_set<int>a(nums.begin(),nums.end());
        ListNode *ans=new ListNode(-1,head);
        ListNode *node=ans;
        while(node!=NULL){
            while(node->next!=NULL and a.count(node->next->val))
                node->next=node->next->next;
            node=node->next;
        }
        return ans->next;
    }
};
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode* curr = &head;
        while(l1 != NULL || l2 != NULL){
            if(l1 == NULL){
                curr->next = l2;
                curr = l2;
                l2 = l2->next;
            } else if(l2 == NULL){
                curr->next = l1;
                curr = l1;
                l1 = l1->next;
            } else if(l2->val <= l1->val){
                curr->next = l2;
                curr = l2;
                l2 = l2->next;
            } else if(l1-> val < l2->val){
                curr->next = l1;
                curr = l1;
                l1 = l1->next;
            }
        }
        return head.next;
    }
};

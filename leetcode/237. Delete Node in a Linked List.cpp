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
    void deleteNode(ListNode* node) {
        ListNode dummy(0);
        ListNode *last = &dummy;
        last->next = node;
        while(node->next != NULL){
            node->val = node->next->val;
            last = node;
            node = node->next;
        }
        last->next = NULL;
    }
};

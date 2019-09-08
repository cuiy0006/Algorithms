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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        
        ListNode* odd_head = head;
        ListNode* even_head = head->next;
        ListNode* odd_tail = odd_head;
        ListNode* even_tail = even_head;
        
        bool is_odd = true;
        ListNode* node = head->next->next;
        while(node != NULL){
            if(is_odd){
                odd_tail->next = node;
                odd_tail = node;
                is_odd = false;
            } else {
                even_tail->next = node;
                even_tail = node;
                is_odd = true;
            }
            node = node->next;
        }
        odd_tail->next = even_head;
        even_tail->next = NULL;
        return odd_head;
    }
};

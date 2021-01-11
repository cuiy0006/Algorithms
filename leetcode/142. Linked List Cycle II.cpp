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
        ListNode* fast = head;
        ListNode* slow = head;
        
        while(fast != nullptr && fast->next != nullptr){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                break;
            }
        }
        
        if(fast == nullptr || fast->next == nullptr){
            return nullptr;
        }
        
        ListNode* slow2 = head;
        while(slow2 != slow){
            slow = slow->next;
            slow2 = slow2->next;
        }
        return slow;
    }
};

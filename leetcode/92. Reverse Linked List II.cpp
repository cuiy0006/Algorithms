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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dummy;
        dummy.next = head;

        ListNode* p = head;
        ListNode* p0 = &dummy;
        int n = 1;
        while (n != left) {
            n += 1;
            p = p->next;
            p0 = p0->next;
        }

        if (p == nullptr || p->next == nullptr) {
            return dummy.next;
        }

        ListNode* first = p;
        ListNode* p1 = p->next;
        ListNode* p2 = p->next;

        while (n != right) {
            n += 1;
            p2 = p2->next;
            p1->next = p;
            p = p1;
            p1 = p2;
        }

        first->next = p2;
        p0->next = p;
        return dummy.next;
    }
};

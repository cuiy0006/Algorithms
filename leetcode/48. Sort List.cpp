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
    ListNode* sortList(ListNode* head) {
        std::vector<std::tuple<int, ListNode*>> v;
        auto p = head;
        while (p != nullptr) {
            v.emplace_back(p->val, p);
            p = p->next;
        }

        std::sort(v.begin(), v.end(), [](auto x, auto y) {
            return std::get<0>(x) < std::get<0>(y);
        });

        ListNode dummy;
        p = &dummy;
        for(auto it = v.begin(); it != v.end(); ++it) {
            p->next = std::get<1>(*it);
            p = p->next;
            p->next = nullptr;
        }
        return dummy.next;
    }
};

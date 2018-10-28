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
        if (!l1) return l2;
        if (!l2) return l1;
        
        ListNode *head;
        if (l1->val < l2->val) {
            head = l1;
            l1 = l1->next;
        } else {
            head = l2;
            l2 = l2->next;
        }
        ListNode *curr = head;
        while(l1 && l2) {
            if(l1->val < l2->val) {
                curr->next = l1;
                l1 = l1->next;
            } else {
                curr->next = l2;
                l2 = l2->next;                
            }
            curr = curr->next;
        }
        curr->next = l1 ? l1 : l2;
        return head;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (&lists == NULL || lists.size() == 0) {
            return NULL;
        }
        if (lists.size() == 1) {
            return lists[0];
        }
        if (lists.size() == 2) {
            return mergeTwoLists(lists[0], lists[1]);
        }
        std::vector<ListNode *> left, right;
        int mid = lists.size() / 2;
        for (int i = 0; i < mid; i++) {
            left.push_back(lists[i]);    
        }
        for (int i = mid; i < lists.size(); i++) {
            right.push_back(lists[i]);    
        }
        ListNode *headRight = mergeKLists(right);
        ListNode *headLeft = mergeKLists(left);
        return mergeTwoLists(headRight, headLeft);
    }
};

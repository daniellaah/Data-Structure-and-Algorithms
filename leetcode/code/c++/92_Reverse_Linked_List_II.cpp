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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode dummyNode(0);
        dummyNode.next = head;
        head = &dummyNode;
        
        ListNode *startPrev = head;
        for(int i=0; i<m-1; i++) {
            startPrev = startPrev->next;
        }
        
        ListNode *curr = startPrev->next;
        ListNode *prev = NULL;
        ListNode *next;
        for(int i=0; i<=(n-m) ; i++) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        startPrev->next->next = curr;
        startPrev->next = prev;
        
        return head->next;
    }
};

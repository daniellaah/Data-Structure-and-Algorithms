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
    ListNode* partition(ListNode* head, int x) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode *leftHead = new ListNode(0);
        ListNode *rightHead = new ListNode(0);
        ListNode *leftCurr = leftHead;
        ListNode *rightCurr = rightHead;
        while (head) {
            if (head->val < x) {
                leftCurr->next = head;
                leftCurr = head;
            } else {
                rightCurr->next = head;
                rightCurr = head;
            }
            head = head->next;
        }
        leftCurr->next = rightHead->next;
        rightCurr->next = NULL;
        return leftHead->next;
    }
};

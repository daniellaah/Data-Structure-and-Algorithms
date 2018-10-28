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
        if (head == NULL || head->next == NULL) {
            return NULL;
        }
        ListNode *fast = head, *slow = head;
        ListNode *meet = NULL;
        while (fast && slow && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (fast == slow) {
                meet = fast;
                break;
            }
        }
        if (meet) {
            while (head != meet) {
                head = head->next;
                meet = meet->next;
            }
            return head;
        } else {
            return NULL;
        }
    }
};

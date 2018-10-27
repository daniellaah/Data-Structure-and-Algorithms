/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// solution 1
class Solution {
public:
    int getListLength(ListNode *head) {
        int i = 0;
        while(head) {
            i++;
            head = head->next;
        }
        return i;
    }
    
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lengthA = getListLength(headA);
        int lengthB = getListLength(headB);
        if(lengthA > lengthB) {
            for(int i=0; i < lengthA-lengthB; i++) {
                headA = headA->next;
            }
        } else {
            for(int i=0; i < lengthB-lengthA; i++) {
                headB = headB->next;
            }            
        }
        while(headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};

// solution 2
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA, *pB = headB;
        while(pA && pB) {
            if(pA == pB) return pA;
            
            pA = pA->next;
            pB = pB->next;
            
            if(pA == pB) return pA;
            
            if(pA == NULL) pA = headB;
            if(pB == NULL) pB = headA;
        }
        return NULL;
    }
};

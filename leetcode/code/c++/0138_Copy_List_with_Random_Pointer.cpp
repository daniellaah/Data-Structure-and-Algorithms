/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
// solution 1, hash, O(n) O(n)
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (!head) {
            return head;
        }
        std::map<RandomListNode *, int> nodeMap;
        std::vector<RandomListNode *> nodeVec;
        RandomListNode *curr = head;
        int i = 0;
        while(curr) { 
            nodeVec.push_back(new RandomListNode(curr->label));
            nodeMap[curr] = i;
            curr = curr->next;
            i++;
        }
        nodeVec.push_back(0);
        curr = head;
        i = 0;
        while(curr) {
            nodeVec[i]->next = nodeVec[i+1];
            if (curr->random) {
                nodeVec[i]->random = nodeVec[nodeMap[curr->random]];
            }
            curr = curr->next;
            i++;
        }
        return nodeVec[0];
    }
};
// solution 2, trick, O(n) O(1)
class Solution {
public:
    RandomListNode *copyNode(RandomListNode *node) {
        RandomListNode *copiedNode;
        copiedNode = new RandomListNode(node->label);
        copiedNode->next = node->next;
        copiedNode->random = node->random;
        return copiedNode;
    }
    
    RandomListNode *copyRandomList(RandomListNode *head) {
        if (!head) {
            return head;
        }
        RandomListNode *curr = head;
        RandomListNode *next;
        RandomListNode *copiedNode;
        while (curr) {
            next = curr->next;
            copiedNode = copyNode(curr);
            copiedNode->next = next;
            curr->next = copiedNode;
            curr = next;
        }
        curr = head;
        while (curr) {
            copiedNode = curr->next;
            if (copiedNode->random) {
                copiedNode->random = copiedNode->random->next;    
            }
            curr = copiedNode->next;
        }
        RandomListNode *prev = head;
        curr = prev->next;
        next = curr->next;
        RandomListNode *copiedHead = curr;
        prev->next = next;
        while (next) {
            curr->next = next->next;    
            prev = next;
            curr = prev->next;
            next = curr->next;
            prev->next = next;
        }
        return copiedHead;
    }
};

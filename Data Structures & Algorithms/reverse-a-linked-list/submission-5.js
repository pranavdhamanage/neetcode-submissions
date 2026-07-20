/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    // reverseList(head) {
    //     let curr = head;
    //     let prev = null;

    //     while(curr) {
    //         const temp = curr.next;
    //         curr.next = prev;
    //         prev = curr
    //         curr = temp;
    //     }

    //     return prev;
    // }

    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        if(!head) {
            return null;
        }

        let newHead = head;
        if(head.next) {
            newHead = this.reverseList(head.next);
            head.next.next = head
            head.next = null;
        }

        return newHead;
    }
}

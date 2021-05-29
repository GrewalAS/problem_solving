"""
Contains the solution for Leetcode Problem 2. Add Two Numbers, found at: https://leetcode.com/problems/add-two-numbers/

Two attempts were made at solving the problem. Both run in O(max(m,n)), where m = len(l1) and n = len(l2).
The second attempt was made to clean up some of the code in the first attempt and to reduce redundant conditions and redundant code.
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # First Attempt
        # carry = 0
        # start = ListNode()
        # cur = start
        
        # while l1 is not None or l2 is not None:
        #     if l1 is not None and l2 is not None:
        #         ans = l1.val + l2.val + carry
        #         l1 = l1.next
        #         l2 = l2.next
        #     elif l1 is not None:
        #         ans = l1.val + carry
        #         l1 = l1.next
        #     elif l2 is not None:
        #         ans = l2.val + carry
        #         l2 = l2.next
        #     else:
        #         break
                
        #     carry = 0
        #     if ans > 9:
        #         ans %= 10
        #         carry = 1
                
        #     new = ListNode(val=ans)
        #     cur.next = new
        #     cur = new
            
        # if carry > 0:
        #     new = ListNode(val=carry)
        #     cur.next = new
        
        # return start.next
        
        # Second Attempt
        carry = 0
        start = ListNode()
        cur = start
        while l1 is not None or l2 is not None:
            cur.next = ListNode()
            cur = cur.next
            if l1 is not None:
                cur.val = l1.val
                l1 = l1.next
            if l2 is not None:
                cur.val += l2.val
                l2 = l2.next
            
            cur.val += carry
            if cur.val > 9:
                cur.val %= 10
                carry = 1
            else:
                carry = 0
                
        if carry > 0:
            cur.next = ListNode(val=carry)
                
        return start.next

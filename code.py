'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        def rmHeadZero(head):
            if head.data != 0:
                return head
            curr = head
            while curr:
                if curr.data != 0:
                    return curr
                curr = curr.next
            return curr
        
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 
            return prev
            
        revHead1 = reverseList(rmHeadZero(head1))
        revHead2 = reverseList(rmHeadZero(head2))
        
        newNode = Node(-1)
        curr = newNode
        carry = 0
        while revHead1 or revHead2:
            val1 = 0
            if revHead1:
                val1 = revHead1.data
                revHead1 = revHead1.next
            val2 = 0
            if revHead2:
                val2 = revHead2.data
                revHead2 = revHead2.next
            sum = val1+val2+carry
            if sum > 9:
                carry=1
                sum = sum-10
            else:
                carry = 0
            curr.next = Node(sum)
            curr = curr.next
        if carry > 0:
            curr.next = Node(1)
        answer = reverseList(newNode.next)
        return answer
            
            
            
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def swapPairs(self, head):
        if head == None:
            return None
        if head.next == None:
            return head

        node1, node2, node3, = head, head.next, None
        while True:
            node1.next = node2.next
            node2.next = node1
            if node3 == None:
                head = node2
            else:
                node3.next = node2
            node3 = node1
            node1 = node1.next

            if node1 == None:
                break
            node2 = node2.next.next.next
            if node2 == None:
                break

        return head

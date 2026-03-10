class Solution:
    def addTwoNumbers(self, l1, l2):

        a=[]
        b=[]

        while l1:
            a.append(l1.val)
            l1=l1.next

        while l2:
            b.append(l2.val)
            l2=l2.next

        a.reverse()
        b.reverse()

        n=int("".join(map(str,a)))
        m=int("".join(map(str,b)))

        s=str(n+m)[::-1]

        dummy=ListNode()
        cur=dummy

        for i in s:
            cur.next=ListNode(int(i))
            cur=cur.next

        return dummy.next


def ex_for_node():
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


        # Creating 3 nodes
        n3 = ListNode(30)
        n2 = ListNode(20, n3)
        n1 = ListNode(10, n2)

        head = n1   # start of the linked list


        # Loop to print values
        node = head
        while node:
            print(node.val)
            node = node.next
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
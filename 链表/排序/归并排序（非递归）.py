#148. Sort List  https://leetcode.com/problems/sort-list/
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        ##求出链表长度
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n +=1
        #即长度 为n
        i = 1
        while (i<n):
            cur = dummy
            j = 0
            #print("i的值",i,"cur的值",cur.val,cur)
            while (j+i<n):
                left = cur.next
                right = cur.next
                for k in range(i):
                    right = right.next
                l,r = 0,0
                while (l<i and r<i and right):
                    if left.val <right.val:
                        cur.next = left
                        cur = cur.next
                        left = left.next
                        l+=1
                    else:
                        cur.next = right 
                        cur = cur.next
                        right = right.next
                        r +=1
                while l<i:
                    cur.next = left
                    cur = cur.next
                    left = left.next
                    l +=1
                while r<i and right:
                    cur.next = right
                    cur = right
                    right = right.next
                    r +=1
                cur.next = right
                j +=i*2
            i *=2
        return dummy.next

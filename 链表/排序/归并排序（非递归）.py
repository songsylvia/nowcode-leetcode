#148. Sort List  https://leetcode.com/problems/sort-list/
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def sortList(self,head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n +=1
        ###总结点数量为n
        i = 1
        while (i<n):
            cur = dummy
            j = 0
            while (j+i)<n:
                left = cur.next
                right = cur.next
                for k in range(i):
                    right = right.next
                #左右分别放到了该放的位置
                l,r = 0,0
                while l<i and r<i and right:
                    if left.val<right.val:
                        cur.next = left
                        cur = cur.next
                        left = left.next
                        l += 1
                    else:
                        cur.next = right
                        cur = cur.next
                        right = right.next
                        r +=1
                while l < i:
                    cur.next = left
                    cur = cur.next
                    left = left.next
                    l +=1
                while r<i and right:
                    cur.next = right
                    cur = cur.next
                    right = right.next
                    r += 1
                cur.next = right
                j += i*2
            i *= 2
        return dummy.next


if __name__ == '__main__':
    head = ListNode(5)
    head.next = ListNode(4)
    head.next.next = ListNode(11)
    head.next.next.next = ListNode(0)
    res = Solution().sortList(head)
    print(res.val)

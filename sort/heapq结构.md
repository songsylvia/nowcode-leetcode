```
import heapq
import random
li = list(range(10))
print(li)
random.shuffle(li)
print(li)
heapq.heapify(li)#建立的是小根堆
print(li)
n = len(li)
for i in range(n):
	print(heapq.heappop(li),end =',')
print("  ")
'''
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.
'''
h = []
heapq.heappush(h,(5,'a'))
heapq.heappush(h,(4,'b'))
heapq.heappush(h,(6,'c'))
print(heapq.heappop(h))
```
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[7, 0, 1, 2, 4, 3, 8, 6, 5, 9]
[0, 2, 1, 5, 4, 3, 8, 6, 7, 9]
0,1,2,3,4,5,6,7,8,9,  
(4, 'b')
[Finished in 0.2s]

```

'''
这是小根堆
heap =[]
heappush(heap,item)
item = heappop(heap)#从堆顶弹出最小的元素
item = heap[0]
heapify(x)把listx转换成heap,in-place
item = heapreplace(heap,item)弹出和返回最小元素，然后加上新的元素，堆大小不改变
'''

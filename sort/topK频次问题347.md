出现频次最高的k个数
```
import collections
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)
```

```
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        count_list = dict()
        for i in nums:
            count_list[i] = count_list.get(i, 0) + 1
        print(count_list)
        p = list()
        for i in count_list.items():
            if len(p) == k:
                if i[1] > p[0][0]:
                    heapq.heappop(p)
                    heapq.heappush(p, (i[1], i[0]))
            else:
                heapq.heappush(p, (i[1], i[0]))

        return [i[1] for i in p]
```
        

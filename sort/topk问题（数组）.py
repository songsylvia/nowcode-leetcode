#看是较大的k个数还是较小的k个数。
#前者建立大小为k的小根堆，后者建立大根堆。后面的数与堆顶元素进行比较，看是否替换堆顶。如果替换，再进行堆调整，然后插入下一个元素

```
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k == 0 or len(tinput)<k:
            return []
        # write code here
        for i in range(k//2-1,-1,-1):
            self.heapmaxadjust(i,k,tinput)#建立成为了一个基本的大根堆
        for j in range(k,len(tinput)):
            if tinput[0]>tinput[j]:
                tinput[0],tinput[j] = tinput[j],tinput[0]#替换同时对大根堆做一次调整
                self.heapmaxadjust(0,k,tinput)
        print(tinput)
        #还需要遍历一遍heap,才能把最后k个元素给放好,大根堆对顶
        #元素最大所以放到最后，然后减少这个元素后的序列重新堆调整，直到长度为0
        for i in range(k-1,-1,-1):
            tinput[0],tinput[i] = tinput[i],tinput[0]
            self.heapmaxadjust(0,i,tinput)
        print(tinput)
        res = []
        for i in range(k):
            res.append(tinput[i])
        return res
    def heapmaxadjust(self,parent,length,nums):
        temp = nums[parent]
        children = parent*2+1
        while (children<length):
            if children +1<length and nums[children]<nums[children+1]:
                   children +=1
            if temp > nums[children]:
                break
            nums[parent] = nums[children]
            parent = children
            children = 2*parent +1
        nums[parent] = temp
        
```

### 【题目】
写一个高效算法，在矩阵中查找一个数是否存在。矩阵有如下特点：

矩阵中每行的数，从左到右单调递增；
每行行首的数大于上一行行尾的数；

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        nums = [i for j in matrix for i in j]
        l = 0
        r = len(nums)-1
        while(l<r):
            mid = l+(r-l-1)//2
            if (nums[mid]<target):
                l = mid+1
            else:
                r = mid
        return nums[l]==target
    ##如果不用辅助数组也用二分的话只要把nums[mid]变成matrix[mid//len(matrix)][mid%len(matrix)]
```
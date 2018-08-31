
# 冒泡排序


**原理**：
    比较两个相邻的元素，将值大的元素交换至右端。
    
**思路**：
	依次比较相邻的两个数，将小数放在前面，大数放在后面。即在第一趟：首先比较第1个和第2个数，将小数放前，大数放后。
	然后比较第2个数和第3个数，将小数放前，大数放后，如此继续，直至比较最后两个数，将小数放前，大数放后。重复第一趟步骤，直至全部排序完成。
 ```
	N个数字要排序完成，总共进行N-1趟排序，每i趟的排序次数为(N-i)次，所以可以用双重循环语句，外层控制循环多少趟，内层控制每一趟的循环次数，即
		for(int i=1;i<arr.length;i++){
			 for(int j=1;j<arr.length-i;j++){
							//交换位置
				}
         }
 ```
    
**优点**：	
    每进行一次排序，就会少比较一次。因为每进行一趟排序都会找出一个较大值。
    第一趟比较之后，排在最后的一个数一定是最大的一个数，第二趟排序的时候，只需要比较除了最后一个数以外的其他的数，
    同样也能找出一个最大的数排在参与第二趟比较的数后面，第三趟比较的时候，只需要比较除了最后两个数以外的其他的数，
    以此类推……也就是说，没进行一趟比较，每一趟少比较一次，一定程度上减少了算法的量。
    
**时间复杂度**：
    1.如果我们的数据正序，只需要走一趟即可完成排序。所需的比较次数C和记录移动次数M均达到最小值，
      即：Cmin=n-1;Mmin=0;所以，冒泡排序最好的时间复杂度为O(n)。
    2.如果很不幸我们的数据是反序的，则需要进行n-1趟排序。每趟排序要进行n-i次比较(1≤i≤n-1)，
      且每次比较都必须移动记录三次来达到交换记录位置。在这种情况下，比较和移动次数均达到最大值：
      
			
      $$C_{max}= \frac{n(n-1)}{2}=O(n^{2})$$
     
      $$M_{max}= \frac{3n(n-1)}{2}=O(n^{2})$$   
      
当原始序列杂乱无序时，冒泡排序的平均时间复杂度为O(n^2)
综上所述：冒泡排序总的平均时间复杂度为：O(n^2). 空间复杂度为O(n),额外为O(1)
   
# 选择排序

**原理**：
        从未排序序列中找出最小（大）值，放到起始位置。然后从剩余未排序的序列中找出最小（大）值，放到已排序序列的末尾，以此类推，直到所有元素全排序完毕。
        
**思路**
        (1)开始时整个线性表为无序表,有序表为空.
        (2)将无序表的第一个元素A[0]与其后的每个元素A[i] (i=1,2,3…n)作比较, 若A[0]较大,将A[i]交换.最后得到的第一个元素将是整个线性表中最小的元素.这样有序表元素+1,无序表元素-1;
        (3)重复第(2)步,直到无序表长度为0;
```
public static void selection_sort(int[] arr) {
	int i, j, min, temp, len = arr.length;
	for (i = 0; i < len - 1; i++) {
		min = i;//未排序序列中最小数据数组下标
		for (j = i + 1; j < len; j++)//在未排序元素中继续寻找最小元素，并保存其下标
			if (arr[min] > arr[j]){
				min = j;}
		temp = arr[min]; //将最小元素放到已排序序列的末尾
		arr[min] = arr[i];
		arr[i] = temp;
	}
}
```

**优点**
        选择排序主要与数据移动有关。
        简单选择排列与序列的初始排序无关。
        如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，它们当中至少有一个将被移到其最终位置上。因此对 n个元素的表进行排序总共进行至多 n-1次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

**时间复杂度**
      简单选择排列与序列的初始排序无关。假设待排序的序列有 N 个元素，则比较次数永远都是N (N - 1) / 2。但移动次数与序列的初始排序有关。当序列正序时，移动次数最少，为 0。当序列反序时，移动次数最多，为n-1次。
      交换次数比冒泡排序较少，由于交换所需CPU时间比比较所需的CPU时间多，n值较小时，选择排序比冒泡排序快。
      原地操作几乎是选择排序的唯一优点，当空间复杂度要求较高时，可以考虑选择排序；实际适用的场合非常罕见。
      所以，总的时间复杂度为O(N^2),空间复杂度为O(n),额外空间复杂度为O(1)
	

# 插入排序

**原理**
通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序包括：直接插入排序、二分插入排序以及希尔排序。

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
（1）从第一个元素开始，该元素可以认为已经被排序
（2）取出下一个元素，在已经排序的元素序列中从后向前扫描
（3）如果该元素（已排序）大于新元素，将该元素移到下一位置
（4）重复步骤3，直到找到已排序的元素小于或者等于新元素的位置，将新元素插入到该位置后
（5）重复步骤2~5

**思路**
**直接插入**
把temp与arr[j]比较，得arr[j]>temp,则把j上的元素往后移出位置插入其他元素,j指针继续往前移.

注意[0,i-1]都是有序的。如果待插入元素比arr[i-1]还大则无需再与[i-1]前面的元素进行比较了.
```
public void insert(int[] a)
	{
		for(int i=1;i<a.length;i++)     //n-1此扫描，依次向前插入n-1个元素
		{
			int temp=a[i];       //每趟将a[i]插入到前面的排序子序列中
			int j;
			for(j=i-1;j>=0&&temp<a[j];j--)
			{
				a[j+1]=a[j];  //将前面较大的元素向后移动 ，把比temp大或相等的元素全部往后移动一个位置 
			}
			a[j+1]=temp;      //temp值到达插入位置，把待排序的元素temp插入腾出位置的(j+1)
			
		}
	}
```

在直接插入排序的基础上，如果数据量比较大，为了减少关键码的比较次数，可以使用折半插入来寻找要插入的位置.
```
public static void main(String[] args) {
		int[] a = {23,45,3,6,7,5};
		for (int i = 1; i < a.length; i++) {
			int left = 0 ;
			int right = i-1;
			int temp = a[i];
			while(left<=right){             // 利用折半查找插入位置
				int mid = (left+right)/2;   // 取中点
				if(a[mid]>temp)             // 插入值小于中点值
					right = mid-1;          // 向左缩小区间
				else 
					left = mid+1;           // 向右缩小区间
			}
			// left即为找到的要插入的位置，所以下边的循环将left-(i-1)位置的元素依次向后移动
			for (int j = i-1; j>=left; j--){ 
				a[j+1] = a[j];
			}
				a[left] = temp;    // 将temp插入到left位置
		}
		for (int i : a) {
			System.out.println(i);
		}
	}
```
**二分插入**
折半查找比顺序查找快，所以折半插入排序就平均性能来说比直接插入排序要快，它所需要的关键码比较次数与待排序记录的初始排列无关，仅依赖
与记录个数，比较次数约等于nlogn次。当n较大时，总关键码比较次数比直接插入比较次数的最坏情况（n平方）/4要好很多，但比其最好情况
2（n-1）要差，所以在记录的初始排列已经接近有序时，直接插入排序比折半插入排序执行的关键码比较次数要少。



**优点**


**时间复杂度**

*如果序列本来是排好序的，那么会触发最好情况。这时只需要n-1次比较即可，没有任何元素移动。所以最好情况下时间复杂度是 O(n).

*如果序列是逆序排列的，那么会触发最坏情况。这时每个元素都需要一步一步地挪到序列首部。所以最坏情况下的时间复杂度是 O(n^2).

平均情况下的时间复杂度是 O(n^2)，对于几百个元素仍然是很快速的算法，因为实现简单。所以STL中的qsort都会以插入排序作为快速排序的
补充来处理少量元素.
空间复杂度当然是 O(1) 的，插入排序是采用迭代策略实现的，只用了常数个变量而已.

# 快速排序
**原理**
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

步骤为：

从数列中挑出一个元素，称为"基准"（pivot），
重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

**思路**
https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Quicksort-diagram.svg/200px-Quicksort-diagram.svg.png
有争议
There can be many ways to do partition, following pseudo code adopts the method given in CLRS book. The logic is simple, 
we start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we 
find a smaller element, we swap current element with arr[i]. Otherwise we ignore current element.

https://www.geeksforgeeks.org/quick-sort/

import java.util.*;

public class QuickSort {
    public int[] quickSort(int[] A, int n) {
        // write code here
        if(A== null || n < 2)
            return A;
        sort(A,0,n-1);
        return A;
    }
    private void sort(int []A,int low ,int high){
        if( low < high){
            int pi = partition(A,low,high);
            sort(A,low,pi-1);//before pi
            sort(A,pi+1,high);// After pi
        }
    }
    public int partition(int[]A,int low,int high){
        int pivot = A[high];
        int i = (low-1);//index of smaller element
        for(int j= low;j<high;j++){
            //如果当前元素小于等于基准元素
            if (A[j]<= pivot)
            {
                i++;
                //swap arr[i] and arr[j]
                int temp = A[i];
                A[i] = A[j];
                A[j] = temp;
            }
        }
        //交换A[i+1]和A[high]
        int temp = A[i+1];
        A[i+1] = A[high];
        A[high] = temp;
        return i+1;
    }
}

**优点**

优点：极快，数据移动少；
缺点：不稳定。

**时间复杂度**
时间复杂度O(N)
空间复杂度O(nlogn)
** NOTE **

快速排序是二叉查找树（二叉搜索树）的一个空间最优化版本。不是循序地把数据项插入到一个明确的树中，而是由快速排序组织这些数据项到一个由递归调用所隐含的树中。这两个算法完全地产生相同的比较次数，但是顺序不同。对于排序算法的稳定性指标，原地分区版本的快速排序算法是不稳定的。其他变种是可以通过牺牲性能和空间来维护稳定性的。

快速排序的最直接竞争者是堆排序（Heapsort）。堆排序通常比快速排序稍微慢，但是最坏情况的运行时间总是 {\displaystyle O(n\log n)} {\displaystyle O(n\log n)}。快速排序是经常比较快，除了introsort变化版本外，仍然有最坏情况性能的机会。如果事先知道堆排序将会是需要使用的，那么直接地使用堆排序比等待introsort再切换到它还要快。堆排序也拥有重要的特点，仅使用固定额外的空间（堆排序是原地排序），而即使是最佳的快速排序变化版本也需要 {\displaystyle \Theta (\log n)} {\displaystyle \Theta (\log n)}的空间。然而，堆排序需要有效率的随机存取才能变成可行。

快速排序也与归并排序（Mergesort）竞争，这是另外一种递归排序算法，但有坏情况 {\displaystyle O(n\log n)} {\displaystyle O(n\log n)}运行时间的优势。不像快速排序或堆排序，归并排序是一个稳定排序，且可以轻易地被采用在链表（linked list）和存储在慢速访问媒体上像是磁盘存储或网络连接存储的非常巨大数列。尽管快速排序可以被重新改写使用在链串列上，但是它通常会因为无法随机存取而导致差的基准选择。归并排序的主要缺点，是在最佳情况下需要 {\displaystyle \Omega (n)} {\displaystyle \Omega (n)}额外的空间。


# 归并排序
**原理**

https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F

该算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。
**思路**


**递归法（Top-down）**
申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
设定两个指针，最初位置分别为两个已经排序序列的起始位置
比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
重复步骤3直到某一指针到达序列尾
将另一序列剩下的所有元素直接复制到合并序列尾

**迭代法（Bottom-up）**
原理如下（假设序列共有 {\displaystyle n} n个元素）：
将序列每相邻两个数字进行归并操作，形成 {\displaystyle ceil(n/2)} {\displaystyle ceil(n/2)}个序列，排序后每个序列包含两/一个元素
若此时序列数不是1个则将上述序列再次归并，形成 {\displaystyle ceil(n/4)} {\displaystyle ceil(n/4)}个序列，每个序列包含四/三个元素
重复步骤2，直到所有元素排序完毕，即序列数为1

**优点**
优点：归并排序只对相邻的数组元素进行处理，所以相对来说归并排序的速度有可能在某一数据量区域内优于普通快排.
缺点：归并排序占用了大量的内存空间（占用了和原数组等长的空间，一旦待排数组的量非常巨大的话，这完全是致命的缺点）里进行排序操作，所以来说，归并排序在大数据的时候很容易造成内存的溢出。

**时间复杂度**
时间O(nlogn),空间为O(1)


# 堆排序
https://www.youtube.com/watch?v=MtQL_ll5KhQ
**原理**
堆排序（英语：Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
。
**思路**
在堆的数据结构中，堆中的最大值总是位于根节点(在优先队列中使用堆的话堆中的最小值位于根节点)。堆中定义以下几种操作：
最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build_Max_Heap）：将堆所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算


import java.util.*;

public class HeapSort {
    public int[] heapSort(int[] A, int n) {
        // write code here
        headsort(A,n);
        return A;
    }
    public void headAdjust(int []A,int parent,int length){
        int temp=A[parent];//记录父节点值
        int children=parent*2+1;//取出子节点索引
        while(children<length){
            if(children+1<length&&A[children+1]>A[children]){//这里是构建大根堆
                children++;//取两个孩子节点中最大的那个
            }
            if(temp>A[children]){//如果父节点大于孩子节点 则退出 这三个节点满足条件
                break;
            }
	    //循环向子节点进行
            A[parent]=A[children];
            parent=children;
            children=children*2+1;
        }
        A[parent]=temp;//把最初的父节点放回二叉树中
    }
    public void headsort(int []A,int n){
        for(int i=n/2-1;i>=0;i--){//构建初始堆 从2/n开始调整二叉树
           headAdjust(A,i,A.length);
        }
        //从堆里把元素一个一个取出来
        for(int i=n-1;i>0;i--){
            //把堆顶元素也就是最大值放到最后，然后每次进行一次堆调整
            swap(A,0,i);
            headAdjust(A,0,i);
        }
    }
    public void swap(int []A,int a,int b){
        int temp=A[a];
        A[a]=A[b];
        A[b]=temp;
    }
}

**优点**


**时间复杂度**
堆排序的平均时间复杂度为 O(nlogn)，空间复杂度为 O(1)

# 希尔排序

**原理**
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。希尔排序是非稳定排序算法。
希尔排序是基于插入排序的以下两点性质而提出改进方法的：
*插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
*但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位


**思路**
希尔排序是将待排序的数组元素 按下标的一定增量分组 ，分成多个子序列，然后对各个子序列进行直接插入排序算法排序；然后依次缩减增量再进行排序，直到增量为1时，进行最后一次直接插入排序，排序结束。

import java.util.*;

public class ShellSort {
    public int[] shellSort(int[] A, int n) {
        // write code here
        if (A==null || n <2)
            return A;
        for (int gap = n/2;gap>0;gap/=2){
            for (int i= gap;i<n;i+=1){
                int temp = A[i];
                int j;
                for (j =i;j>=gap&& A[j-gap]>temp;j-=gap)
                    A[j] = A[j-gap];
                A[j] = temp;
            }
        }
        return A;
    }
}

**优点**
希尔算法在最坏的情况下和平均情况下执行效率相差不是很多，与此同时快速排序在最坏的情况下执行的效率会非常差。希尔排序没有快速排序算法快，因此中等大小规模表现良好，对规模非常大的数据排序不是最优选择。
（注：专家们提倡，几乎任何排序工作在开始时都可以用希尔排序，若在实际使用中证明它不够快，再改成快速排序这样更高级的排序算法。）

**时间复杂度**
希尔排序耗时的操作有：比较 + 后移赋值。

时间复杂度情况如下：（n指待排序序列长度）
1) 最好情况：序列是正序排列，在这种情况下，需要进行的比较操作需（n-1）次。后移赋值操作为0次。即O(n)
2) 最坏情况：O(nlog2n)。
3) 渐进时间复杂度（平均时间复杂度）：O(nlog2n)

希尔排序是按照不同步长对元素进行插入排序，当刚开始元素很无序的时候，步长最大，所以插入排序的元素个数很少，速度很快；当元素基本有序了，步长很小，插入排序对于有序的序列效率很高。所以，希尔排序的时间复杂度会比O(n²)好一些。
希尔算法的性能与所选取的增量（分组长度）序列有很大关系。只对特定的待排序记录序列，可以准确地估算比较次数和移动次数。想要弄清比较次数和记录移动次数与增量选择之间的关系，并给出完整的数学分析，至今仍然是数学难题。

# 计数排序
**https://www.youtube.com/watch?v=7zuGmKfUt7s**非常清楚的讲解
Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
Auxiliary Space: O(n+k)

Points to be noted:
1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.
2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data.
3. It is often used as a sub-routine to another sorting algorithm like radix sort.
4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1).
5. Counting sort can be extended to work for negative inputs also.


**原理**
计数排序（Counting sort）是一种稳定的线性时间排序算法。计数排序使用一个额外的数组 C ，其中第i个元素是待排序数组i的元素的个数。然后根据数组  C 来将 A中的元素排到正确的位置。

**思路**
由于用来计数的数组 C 的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，需要大量时间和内存。例如：计数排序是用来排序0到100之间的数字的最好的算法，但是它不适合按字母顺序排序人名。但是，计数排序可以用在基数排序算法中，能够更有效的排序数据范围很大的数组。

通俗地理解，例如有10个年龄不同的人，统计出有8个人的年龄比A小，那A的年龄就排在第9位，用这个方法可以得到其他每个人的位置，也就排好了序。当然，年龄有重复时需要特殊处理（保证稳定性），这就是为什么最后要反向填充目标数组，以及将每个数字的统计减去1的原因。算法的步骤如下：

找出待排序的数组中最大和最小的元素
统计数组中每个值为 i的元素出现的次数，存入数组C 的第 i项
对所有的计数累加（从 C 中的第一个元素开始，每一项和前一项相加）
反向填充目标数组：将每个元素 i放在新数组的第  C[i]}项，每放一个元素就将C[i]减去1

import java.util.*;

public class CountingSort {
    public int[] countingSort(int[] A, int n) {
        // write code here
        if (A == null || n<2){
            return A;
        }
        int min = A[0];
        int max = A[0];
        //遍历数组，找到最大值和最小值
        for (int i = 0;i< n;i++){
            if (max < A[i])
                max = A[i];
            if (min > A[i])
                min = A[i];
        }
        //根据最大值最小值建立一个数组表示桶
        int temp[] = new int [max-min+1];
        //遍历数组中的值放入桶中，同时桶数组记录数量,这时用桶数组的下标表示目标数组和最小值的差别,桶数组中存放数量
        for (int i = 0;i<n;i++){
            temp[A[i]-min] ++;
        }
        //存放完成后将桶中数字依次倒出,
        int index = 0; //表示下标
        for(int i=0;i<max-min+1;i++){
            while(temp[i] > 0){
                //从桶中取出一个树
                A[index] = i + min;
                index++;
                //桶中数量减一
                temp[i]--;
            }
        }
        return A;
    }
}

**优点**


**时间复杂度**
当输入的元素是 0 到k之间的整数时，它的运行时间是 {\displaystyle \Theta (n+k)} {\displaystyle \Theta (n+k)}。计数排序不是比较排序，排序的速度快于任何比较排序算法。

# 基数排序
https://www.youtube.com/watch?v=nu4gDuFabIM
https://www.geeksforgeeks.org/radix-sort/

**原理**
https://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F
将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。
它是这样实现的：将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。
**思路**
import java.util.*;

public class RadixSort {
    public int[] radixSort(int[] A, int n) {
        // write code here
        int[][] tmp = new int[10][n];//排序桶用于保存每次排序后的结果，这一位上排序结果相同的数字放在同一个桶里
        int[] count = new int[10];////用于保存每个桶里有多少个数字
        int i = 1;
        while(i <1000){//将数组A里的每个数字放在相应的桶里
            for(int j = 0; j < n; j++){
                int pos = A[j]/i%10;//某一位是多大的数字
                tmp[pos][count[pos]++] = A[j];//
            }
            int index = 0;
            for(int k = 0;k<10;k++){//将前一个循环生成的桶里的数据覆盖到原数组中用于保存这一位的排序结果
                for(int m = 0;m<count[k];m++){//这个桶里有数据，从上到下遍历这个桶并将数据保存到原数组中
                    A[index++] = tmp[k][m];
                }
                count[k] = 0;//将桶里计数器置0，用于下一次位排序
            }
            i *= 10; 
        }
        return A;
    }
}
**优点**
基数排序的时间复杂度是 O(kn)，其中n是排序元素个数，k是数字位数。注意这不是说这个时间复杂度一定优于O(nlogn)， k的大小取决于数字位的选择（比如比特位数），和待排序数据所属数据类型的全集的大小；k决定了进行多少轮处理，而 n是每轮处理的操作数目。

以排序 n个不同整数来举例，假定这些整数以B为底，这样每位数都有 B个不同的数字, k=\log _{B}N


N是待排序数据类型全集的势。虽然有B个不同的数字，需要B个不同的桶，但在每一轮处理中，判断每个待排序数据项只需要一次计算确定对应数位的值，因此在每一轮处理的时候都需要平均 n次操作来把整数放到合适的桶中去，所以就有：

k\approx= log _{B}N
所以，基数排序的平均时间T就是：
T\approx= log _{B}(N)\cdot n}

其中前一项是一个与输入数据无关的常数，当然该项不一定小于 log n。

如果考虑和比较排序进行对照，基数排序的形式复杂度虽然不一定更小，但由于不进行比较，因此其基本操作的代价较小，而且在适当选择的 B之下, k一般不大于log n，所以基数排序一般要快过基于比较的排序，比如快速排序。

**时间复杂度**


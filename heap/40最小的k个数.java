package 剑指offer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
/*获取最小的k个数
 * 思路一：排序后，位于前面的k个数就是最小的K个数
 * 思路二：partition方法。选第k个数作为pivot，如果比它小放他的左边，大放右边。这样调整之后，位于中间左边的k个数字就是最小的
 * 思路三：特别适合处理海量数据O(nlogk):
 * 先建一个size为k的大根堆，然后如果还有数添加，与堆顶比较，
 * 如果大于堆顶，说明这个数不可能是最小的k个数
 * 如果小于堆顶，则把堆顶删除并把这个数添加至堆里面，重新调整堆的大小。
 * O(1)得到已有的k个数字中最大值；特别用O(logK)完成删除及插入
 * 总的时间复杂度为O(NlogK)
 * 
 * 
 * 
 * 
 */
public class topk40 {
	public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
		ArrayList<Integer> res = new ArrayList<>();//这是牛客网上刷题时要求的方法
		if(input == null||input.length<=0||k>input.length){
			return res;
		}
		PriorityQueue<Integer> maxheap = new PriorityQueue<Integer>(k,new Comparator<Integer>(){
			

			@Override
			public int compare(Integer o1, Integer o2) {
				// TODO 自动生成的方法存根
				return o2 -o1;
			}
		}
		);
		for(int i =0;i<input.length;i++){
			if(maxheap.size()<k){
				maxheap.offer(input[i]);
			}else{
				if(maxheap.peek()>input[i]){
					maxheap.poll();
					maxheap.offer(input[i]);
				}
			}
		}
		for(Integer integer:maxheap){
			res.add(integer);
		}
		return res;
        
    }
	public static void main(String[] args) {
	}
}
/*面试时如果不能用优先级队列的话
 * public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        if (input == null ||input.length<=0||k>input.length)return res;
        //构建最大堆
        for(int len =k/2-1;len >= 0;len--){
            adjustMaxHeap(input,len,k-1);
        }
        //从第k个元素开始分别于最大堆的最大值进行比较，如果小，就交换该值与最大堆的最大值，
        //最终堆里的就是最小的k个数
        for(int i = k;i<input.length;i++){
            if (input[i]<input[0]){
                int temp = input[0];
                input[0] = input[i];
                input[i] = temp;
                adjustMaxHeap(input ,0,k-1);
            }
        }
        //将调整好的前k个数放进链表中
        for (int j = 0;j<k;j++){
            res.add(input[j]);
        }
        return res;
    }
    //构建大顶堆
    public void adjustMaxHeap(int[]input,int pos,int length){
        int temp;//先把最上面根节点保存了
        int child;
        for (temp = input[pos];2*pos+1<=length;pos= child){
            child = 2*pos+1;
            //child 可以等于length但是下面的程序不能，我们还要判断child 和child+1呢
            //找最大的子节点与父节点比较，如果子节点大于父节点则交换,否则则退出
            if (child <length&&input[child]<input[child+1]){
                child++;
            }
            if (input[child]>temp){
                input[pos] = input[child];
            }else{
                break;
            }
        }
        input[pos] = temp;
    }
}
 * 
 * 
 * 
 * 
 * 
 */



/*笔试最快速度，但不是最佳方法
import java.util.Scanner;

public class topk40{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in );
        String a = sc.nextLine();
        sc.close();
        String[] b = a.split(" ");
        int []A = new int[b.length-1];
        for(int i =0;i<b.length-1;i++){
        	A[i] =Integer.parseInt(b[i]);	
        }
        int k = Integer.parseInt(b[b.length-1]);
        Arrays.sort(A);
        for(int i =0;i<k;i++){
        	System.out.println(A[i]);
        }
    }
    
    
}*/

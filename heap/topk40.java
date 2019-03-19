package ��ָoffer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
/*��ȡ��С��k����
 * ˼·һ�������λ��ǰ���k����������С��K����
 * ˼·����partition������ѡ��k������Ϊpivot���������С��������ߣ�����ұߡ���������֮��λ���м���ߵ�k�����־�����С��
 * ˼·�����ر��ʺϴ���������O(nlogk):
 * �Ƚ�һ��sizeΪk�Ĵ���ѣ�Ȼ�������������ӣ���Ѷ��Ƚϣ�
 * ������ڶѶ���˵�����������������С��k����
 * ���С�ڶѶ�����ѶѶ�ɾ���������������������棬���µ����ѵĴ�С��
 * O(1)�õ����е�k�����������ֵ���ر���O(logK)���ɾ��������
 * �ܵ�ʱ�临�Ӷ�ΪO(NlogK)
 * 
 * 
 * 
 * 
 */
public class topk40 {
	public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
		ArrayList<Integer> res = new ArrayList<>();//����ţ������ˢ��ʱҪ��ķ���
		if(input == null||input.length<=0||k>input.length){
			return res;
		}
		PriorityQueue<Integer> maxheap = new PriorityQueue<Integer>(k,new Comparator<Integer>(){
			

			@Override
			public int compare(Integer o1, Integer o2) {
				// TODO �Զ����ɵķ������
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
/*����ʱ������������ȼ����еĻ�
 * public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        if (input == null ||input.length<=0||k>input.length)return res;
        //��������
        for(int len =k/2-1;len >= 0;len--){
            adjustMaxHeap(input,len,k-1);
        }
        //�ӵ�k��Ԫ�ؿ�ʼ�ֱ������ѵ����ֵ���бȽϣ����С���ͽ�����ֵ�����ѵ����ֵ��
        //���ն���ľ�����С��k����
        for(int i = k;i<input.length;i++){
            if (input[i]<input[0]){
                int temp = input[0];
                input[0] = input[i];
                input[i] = temp;
                adjustMaxHeap(input ,0,k-1);
            }
        }
        //�������õ�ǰk�����Ž�������
        for (int j = 0;j<k;j++){
            res.add(input[j]);
        }
        return res;
    }
    //�����󶥶�
    public void adjustMaxHeap(int[]input,int pos,int length){
        int temp;//�Ȱ���������ڵ㱣����
        int child;
        for (temp = input[pos];2*pos+1<=length;pos= child){
            child = 2*pos+1;
            //child ���Ե���length��������ĳ����ܣ����ǻ�Ҫ�ж�child ��child+1��
            //�������ӽڵ��븸�ڵ�Ƚϣ�����ӽڵ���ڸ��ڵ��򽻻�,�������˳�
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



/*��������ٶȣ���������ѷ���
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
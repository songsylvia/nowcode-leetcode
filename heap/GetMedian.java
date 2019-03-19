package ��ָoffer;

import java.util.Comparator;
import java.util.PriorityQueue;

/*��ȡ�������е���λ��
 * ˼·�������������С���ѣ���λ��Ϊ�Ѷ�Ԫ�ص�ƽ��ֵ
 * �õ�priorityQueue�����ѡ���topk��ָoffer��Ҳ�õ���
 * 
 */
public class GetMedian {
	PriorityQueue <Integer> minheap = new PriorityQueue<>();
	PriorityQueue <Integer> maxheap = new PriorityQueue<>(11,new Comparator<Integer>(){
		public int compare(Integer o1,Integer o2){
			return o2-o1;
		}
	});
	int count = 0;
	public void Insert(Integer num){//Ϊʲô��integer
		count++;
		if(count%2==0){
			//�����ż��
			if(!maxheap.isEmpty()&&num<maxheap.peek()){
				maxheap.offer(num);
				num = maxheap.poll();
			}
			minheap.offer(num);
		}else{
			if(!minheap.isEmpty()&&num>minheap.peek()){
				minheap.offer(num);
				num = minheap.poll();
			}
			maxheap.offer(num);
		}
	}
	public Double Getmedian(){
		if(count == 0){
			throw new RuntimeException("no available num");
		}
		double res = 0;
		if((count&1) ==1){
			res = maxheap.peek();
		}else{
			res = (minheap.peek()+maxheap.peek())/2.0;
		}
		return res;
	}
}

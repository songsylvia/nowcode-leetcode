package basic_class_01;

import java.util.Arrays;

public class Code_03_HeapSort {

	public static void heapSort(int[] arr) {
		if (arr == null || arr.length < 2) {
			return;
		}
		for (int i = 0; i < arr.length; i++) {
			heapInsert(arr, i);//0~i�����˴���ѣ���δ������
		}
		int size = arr.length;
		swap(arr, 0, --size);//���ֵ���������λ�ã���ɾȥ���һ����size--
		while (size > 0) {
			heapify(arr, 0, size);//���µ����ɴ����
			swap(arr, 0, --size);//�ָ㶨���һ����
		}
	}
	//����ʱ���ϵ���
	//�������ʱO(log(i-1))�ܵĸ��Ӷ�ΪO(log1)+O(log2)+O(LOG3)+...+O(logN-1) = O(N)
	public static void heapInsert(int[] arr, int index) {
		while (arr[index] > arr[(index - 1) / 2]) {//��ǰindex�ȸ�λ�ô�
			swap(arr, index, (index - 1) / 2);//������ֱ�����ȸ�λ�ô� 
			index = (index - 1) / 2;//ע��0-1/2��ȻΪ0����ʱ���Ҳ����������
		}
	}
	
//���鷢���仯ʱ����ε���������65435���15435
//���Һ��Ӷ���ʱ���ȿ����Һ����ĸ���Ȼ����֮�ȽϽ���������
	//�����и�size������size�ж��Ƿ�Խ�磬size�ǻ������ģ�0~size-1���γɶѣ����ܣ�
	public static void heapify(int[] arr, int index, int size) {
		int left = index * 2 + 1;//�ҵ�����
		while (left < size) {//left����Խ�磬Խ��˵���Ѿ���Ҷ�ӽڵ���
			int largest = left + 1 < size && arr[left + 1] > arr[left] ? left + 1 : left;
			//�Һ��Ӳ�Խ�磬�����Һ����Ҵ���largesetΪ�Һ��ӣ�����Ϊ����
			largest = arr[largest] > arr[index] ? largest : index;//�뵱ǰindex�Ƚ�
			if (largest == index) {
				break;//���largest���ǵ�ǰindex��˵����ǰֵ�Ѿ��Ǵ���ˣ��������µ�����
			}
			//ifû�У�Ҳ������Ҫ��������
			swap(arr, largest, index);
			index = largest;//�ǰֵΪ���ڵ����ֵ�����ж�
			left = index * 2 + 1;
		}
	}

	public static void swap(int[] arr, int i, int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}

	// for test
	public static void comparator(int[] arr) {
		Arrays.sort(arr);
	}

	// for test
	public static int[] generateRandomArray(int maxSize, int maxValue) {
		int[] arr = new int[(int) ((maxSize + 1) * Math.random())];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = (int) ((maxValue + 1) * Math.random()) - (int) (maxValue * Math.random());
		}
		return arr;
	}

	// for test
	public static int[] copyArray(int[] arr) {
		if (arr == null) {
			return null;
		}
		int[] res = new int[arr.length];
		for (int i = 0; i < arr.length; i++) {
			res[i] = arr[i];
		}
		return res;
	}

	// for test
	public static boolean isEqual(int[] arr1, int[] arr2) {
		if ((arr1 == null && arr2 != null) || (arr1 != null && arr2 == null)) {
			return false;
		}
		if (arr1 == null && arr2 == null) {
			return true;
		}
		if (arr1.length != arr2.length) {
			return false;
		}
		for (int i = 0; i < arr1.length; i++) {
			if (arr1[i] != arr2[i]) {
				return false;
			}
		}
		return true;
	}

	// for test
	public static void printArray(int[] arr) {
		if (arr == null) {
			return;
		}
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}

	// for test
	public static void main(String[] args) {
		int testTime = 500000;
		int maxSize = 100;
		int maxValue = 100;
		boolean succeed = true;
		for (int i = 0; i < testTime; i++) {
			int[] arr1 = generateRandomArray(maxSize, maxValue);
			int[] arr2 = copyArray(arr1);
			heapSort(arr1);
			comparator(arr2);
			if (!isEqual(arr1, arr2)) {
				succeed = false;
				break;
			}
		}
		System.out.println(succeed ? "Nice!" : "Fucking fucked!");

		int[] arr = generateRandomArray(maxSize, maxValue);
		printArray(arr);
		heapSort(arr);
		printArray(arr);
	}

}

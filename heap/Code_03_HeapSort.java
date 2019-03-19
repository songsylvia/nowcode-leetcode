package basic_class_01;

import java.util.Arrays;

public class Code_03_HeapSort {

	public static void heapSort(int[] arr) {
		if (arr == null || arr.length < 2) {
			return;
		}
		for (int i = 0; i < arr.length; i++) {
			heapInsert(arr, i);//0~i建立了大根堆，但未必有序
		}
		int size = arr.length;
		swap(arr, 0, --size);//最大值交换到最后位置，并删去最后一个数size--
		while (size > 0) {
			heapify(arr, 0, size);//重新调整成大根堆
			swap(arr, 0, --size);//又搞定最后一个数
		}
	}
	//建堆时往上调整
	//加入调整时O(log(i-1))总的复杂度为O(log1)+O(log2)+O(LOG3)+...+O(logN-1) = O(N)
	public static void heapInsert(int[] arr, int index) {
		while (arr[index] > arr[(index - 1) / 2]) {//当前index比父位置大
			swap(arr, index, (index - 1) / 2);//交换，直到不比父位置大 
			index = (index - 1) / 2;//注意0-1/2依然为0，此时相等也就跳出来了
		}
	}
	
//数组发生变化时，如何调整如大根堆65435变成15435
//左右孩子都有时，先看左右孩子哪个大然后与之比较交换，继续
	//这里有个size，根据size判断是否越界，size是会伸缩的（0~size-1已形成堆，不管）
	public static void heapify(int[] arr, int index, int size) {
		int left = index * 2 + 1;//找到左孩子
		while (left < size) {//left不能越界，越界说明已经是叶子节点了
			int largest = left + 1 < size && arr[left + 1] > arr[left] ? left + 1 : left;
			//右孩子不越界，且左右孩子右大令largeset为右孩子，否则为左海子
			largest = arr[largest] > arr[index] ? largest : index;//与当前index比较
			if (largest == index) {
				break;//如果largest还是当前index，说明当前值已经是大堆了，不用往下调整了
			}
			//if没中，也就是需要调整交换
			swap(arr, largest, index);
			index = largest;//令当前值为现在的最大值，再判断
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

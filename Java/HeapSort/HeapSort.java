import java.*;
// import java.io.FileReader;
// import java.util.Scanner;
// import java.io.File;
// import java.io.FileNotFoundException;

class Heap {
    public int heap;
    public static int size;
    public static int[] arr;

    Heap() {
        size = 10;
        heap = 0;
        arr = new int[size];
    }

    public void add(int data) {
        if (heap > size)
            return;
        arr[heap] = data;
        sift_up(arr, heap);
        heap++;
    }

    public void delete() {
        if (heap <= 0)
            return;
        arr[0] = arr[heap - 1];
        sift_down(arr, 0);
        heap--;
    }

    public void sift_up(int arr[], int x) {
        if (x != 0) {
            int parentIndex = (x - 1) / 2;
            if (arr[x] < arr[parentIndex]) {
                int temp = arr[parentIndex];
                arr[parentIndex] = arr[x];
                arr[x] = temp;
                sift_up(arr, parentIndex);
            }
        }
    }

    public void sift_down(int arr[], int parentIndex) {

        int left = 2 * parentIndex + 1;
        int right = 2 * parentIndex + 2;
        int min;

        if (left <= heap - 1) {
            if (left == heap - 1) {
                min = left;
            } else {
                if (arr[left] < arr[right]) {
                    min = left;
                } else {
                    min = right;
                }
            }

            if (arr[min] < arr[parentIndex]) {
                int temp = arr[min];
                arr[min] = arr[parentIndex];
                arr[parentIndex] = temp;
                sift_down(arr, min);
            }
        }
    }

    public int[] retArr() {
        return arr;
    }

    public void print() {
        for (int i = 1; i < size / 2; i++) {
            System.out.print("Parent: " + arr[i] + "\nLeft Child: " + arr[2 * i] + "\nRight Child: " + arr[2 * i + 1]);
            System.out.println();
            System.out.println();
        }
    }

    void levelDisplay() {
        int c = 1; // keeps track of count

        int l = 0; // levels
        System.out.print("\nLevel " + l + ": ");
        for (int i = 0; i < heap; i++) {
            if (c != 0) {
                System.out.print(arr[i] + " ");
                c--;
            }
            if (c == 0) {
                l++;
                c = (int) Math.pow(2.0, l);
                System.out.print("\nLevel " + l + ": ");
            }
        }
    }

}

public class HeapSort {
    public static int[] arr;
    public static Heap h = new Heap();

    public static void ReadFromFile() {
        File file = new File("input.txt");
        FileReader reader = null;
        try {
            reader = new FileReader(file);
        } catch (FileNotFoundException e) {
            System.out.println("Cant Read File");
        }
        Scanner input = new Scanner(reader);
        while (input.hasNextLine()) {
            String temp = input.nextLine();
            h.add(Integer.parseInt(temp));
        }
        input.close();
    }

    public static void main(String[] args) {
        ReadFromFile();
        h.levelDisplay();
        h.delete();
        h.delete();
        h.delete();
        h.delete();
        h.delete();
        System.out.println("\nheap Size: " + h.heap);
        h.levelDisplay();
    }
}
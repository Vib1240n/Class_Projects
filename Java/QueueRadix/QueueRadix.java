/*
Vibhore Sagar
Radix Sort Lab
CSc-130-01
 */

class Node {                                                                                                            // Generic Node class begin
     private int data;
     private Node next;
     Node(int data){
         this.data = data;
         this.next = null;
     }

    public void setData(int data) {                                                                                        //  setter for data, sets data
        this.data = data;
    }

    public int getData() {                                                                                                 //  getter for data, return this.data
        return data;
    }

    public void setNext(Node n) {                                                                                     //  setter for next reference, sets next to n
        this.next = n;
    }

    public Node getNext() {                                                                                             //  getter for next reference, returns this.next
        return next;
    }
}

class Queue {                                                                                                           //  Queue class begin
    private Node front;                                                                                                 //  Node reference for front of the queue
    private Node back;                                                                                                  //  Node reference for back of the queue         // initial length of the queue

    public void enqueue(int data,int Index, Queue[] q) {                                                                //  enqueue method to insert values in the queue
        Node newNode = new Node(data);

        if (q[Index].front == null) {                                                                                   //  if the front is null then newNode is front and back
            q[Index].front = newNode;
            q[Index].back = newNode;
        }else {
            q[Index].back.setNext(newNode);                                                                             //  else sets the newNode at the back of the queue
            q[Index].back = newNode;
        }
    }

    public int[] dequeue(Queue[] q, int[] arr) {                                                                        //  dequeue method start, deletes from front of queue and returns value
        Node curr;
        int index = 0;
        int i = 0;
        for(; index < q.length; index++ ){
            if(q[index].front != null){
                while((q[index].front != null) && i < arr.length){
                    curr = q[index].front;
                    arr[i] = curr.getData();
                    q[index].front = q[index].front.getNext();
                    i++;
                }
                if(q[index].front == null){
                    q[index].back = null;
                }
            }
        }
        return arr;
    }
}


class Radix{                                                                                                            //  Radix class start
    int[] ArrayTosort = QueueRadix.ArrayTosort;

    public int[] sort( Queue[] buckets){                                                                                //  Radix sort method start, sorts array using Radix sort algorithm
        int arraySize = ArrayTosort.length;
        int pow10 = 1;
        Queue qSort = new Queue();
        int maxDigits = maxNumber(ArrayTosort);
        while(pow10 <= maxDigits){
            for (int i = 0; i < arraySize; i++) {
                int bIndex = Math.abs(ArrayTosort[i] / pow10) %10;
                qSort.enqueue(ArrayTosort[i],bIndex,buckets);
            }
            ArrayTosort = qSort.dequeue(buckets,ArrayTosort);
            pow10*=10;
        }
        return ArrayTosort;
    }

    public int maxNumber(int[] arr){
        int max = arr[0];
        for(int i = 1; i < arr.length; i++){
            if(max<arr[i]){
                max = arr[i];
            }
        }
        return max;
    }
}

public class QueueRadix {                                                                                                   //  Driver class start
    static int ArrayTosort[] = {170, 45,77, 90, 802, 24, 2, 66,100 ,234,123,4532,13,3,999,888,969};                     //  Global declaration of array to sort


    public static void main(String[] args){                                                                             //  main methods start
        Radix arr = new Radix();
        Queue[] buckets = new Queue[10];
        for (int q = 0; q < 10; q++) {
            buckets[q] = new Queue();
        }
        System.out.print("Original Array: ");
        for(int i = 0; i < ArrayTosort.length; i++){
            System.out.print(ArrayTosort[i]+ " ");                                                                      //  Prints out original contents of the array
        }
        int[] SortedArray = arr.sort(buckets);
        System.out.print("\nArray sorted Ascending: ");
        for(int i = 0; i < SortedArray.length; i++){
            System.out.print(SortedArray[i]+ " ");                                                                      //  Prints out array after sorting in Ascending order
        }
        System.out.print("\nArray sorted descending: ");
        for(int i = SortedArray.length-1; i >=0; i--){
            System.out.print(SortedArray[i]+ " ");                                                                      //  Prints out array in Descending order
        }
    }
}

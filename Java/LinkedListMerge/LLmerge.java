import java.util.Random;
import java.util.Scanner;

class Node{                                                                                                             //  Node class begin
    private Node next;                                                                                                  //  next pointer for node
    private final int data;                                                                                             //  Data for Node to handle

    Node(int data){                                                                                                     //  Node constructor to take in data and initialize node
        this.data = data;
        this.next = null;
    }
    public int getData(){                                                                                               //  Returns data of the node
        return data;
    }
    public Node getNext(){                                                                                              //  Returns next pointer of the Node
        return next;
    }
    public void setNext(Node n){                                                                                        //  changes next/sets new next of the node
        this.next = n;
    }
}

class LinkedList{                                                                                                       //  Linked list class begin
    private Node head = null;                                                                                           //  Initializing Head of the list.
    private Node tail = null;                                                                                           //  Initializing Tail of to add at end
    public void push(int data) {                                                                                        //  addToList method begins- adds the new Node created at the end of the list
        Node newNode = new Node(data);                                                                                  //  Creates a new node and assigns value
        if (head == null) {                                                                                             //  head is null then newNode = head
            head = newNode;                                                                                             //  head and tail are same when head = null
        } else {                                                                                                        //  when head not equal to null
            tail.setNext(newNode);                                                                                      //  tail is newNode
        }
        tail = newNode;
    }
    public void print(){                                                                                                //  Traverse through list and print out its Nodes
        Node curr = head;
        while( curr != null){
            System.out.print(curr.getData()+" ");
            curr = curr.getNext();
        }
        System.out.println("\n");
    }
    public Node head(){                                                                                                 //  Returns head of the list
        return head;
    }
    public void setHead(Node h){                                                                                        //  sets the new head of the list
        this.head = h;
    }
}

class Sort{                                                                                                             //  Sort class begin
    public Node mergeSort(Node temp){                                                                                   //  Merge sort method begins

        Node merged;

        if( temp == null || temp.getNext() == null){
            return temp;
        }

        Node middle = middle(temp);                                                                                     //  Finds the middle of list and assigns pointer to middle node
        Node Next = middle.getNext();                                                                                   //  assigns pointer to the next of the middle node of list
        middle.setNext(null);                                                                                           //  sets the middle node next to null

        Node left= mergeSort(temp);                                                                                     //  keeps breaking the right side of list into half until 1 node is left
        Node right = mergeSort(Next);                                                                                   //  keeps breaking the right side of list into half until 1 node is left
        merged = merge(left, right);                                                                                    //  merges left and right side of the list after sorting
        return merged;                                                                                                  //  returns head pointer of the merged list
    }

    Node merge(Node left, Node right){                                                                                  //  merge method begin
        Node merged;                                                                                                    //  initializing merge pointer to null
        if(left == null){
            return right;
        }
        if( right == null){
            return left;
        }
            if (right.getData() <= left.getData()) {
                merged = right;
                merged.setNext(merge(right.getNext(), left));
            } else {
                merged = left;
                merged.setNext(merge(right, left.getNext()));
            }
        return merged;
    }

    Node  middle(Node temp) {                                                                                           //  splits the list into two by finding the middle node of list
        Node slow = temp, fast = temp.getNext();
        while(fast != null) {
            fast = fast.getNext();
            if (fast != null) {
                slow = slow.getNext();
                fast = fast.getNext();
            }
        }
        return slow;
    }
}


public class LLmerge
 {                                                                                                   //  driver class begins
    public static void main (String[] args){                                                                            //  main method begins
        int upperLimit = 1000;                                                                                          //  maximum limits the numbers can have
        Random rand = new Random();                                                                                     //  Random number generator class object
        LinkedList list = new LinkedList();                                                                             //  Linked list class object
        Sort sort = new Sort();                                                                                         //  Sort class object
        Scanner input = new Scanner(System.in);                                                                         //  Scanner class object
        int random;                                                                                                     //  to store random number
        System.out.print("How many numbers do you want to sort?: ");
        int i = input.nextInt();
        int j = 0;
        while(j != i){
            random = rand.nextInt(upperLimit+1);
            list.push(random);                                                                                          //  pushes random number into list
            j++;
        }
        System.out.print("numbers before Merge Sort: ");                                                                //  prints list before sorting
        list.print();                                                                                                   //  list print method called
        list.setHead(sort.mergeSort(list.head()));                                                                      //  Sorts the list and then sets the head of list to the head of sorted list
        System.out.print("numbers after Merge Sort: ");                                                                 //  prints list after sorting
        list.print();                                                                                                   //  list print method called
        input.close();                                                                                                  //  Scanner class closed
    }
}

import java.util.*;
import java.io.*;


class Node{
    private String name;                                                    // Creating data variables
    private Node next;
    Node(String name) {                                                     //Constructor start- assigns the value and next pointer to null.
        this.name = name;
    }
    public Node getNext(){
        return next;
    }
    public void setName(String name){
        this.name = name;
    }
    public void setNext(Node n){
        next = n;
    }public String getName(){
        return this.name;
    }
}

class Llist {                                                               // Linked list class begins
    private Node head = null;                                               // Initializing Head of the list.
    private Node tail = null;                                               // Initializing Tail of to add at end
    public void addToList(String name) {                                    // addToList method begins- adds the new Node created at the end of the list
        Node newNode = new Node(name);                                      // Creates a new node and assigns value
        if (head == null) {                                                 // head is null then newNode = head
            head = newNode;                                                 // head and tail are same when head = null
            tail = newNode;
        } else {                                                            // when head not equal to null
            tail.setNext(newNode);                                          // tail is newNode
            tail = newNode;
        }
    }
    public int GetLength(){                                                 // Calculates and returns the length of the list
        int Counter = 0;
        Node curr = head;
        while(curr != null){
            Counter++;
            curr = curr.getNext();
        }
        return Counter;
    }
    public void traverse(){                                                 // Traverse through list and print out its Nodes
        Node curr = head;
        int i =1;
        while( curr != null){
            System.out.println(i +". " + curr.getName() + " ");
            curr = curr.getNext();
            i++;
        }
        System.out.println("\n");
    }
    public void Split_Merge(int counter){                                   // Method to split the list into half and make them into new lists.
        int newCounter = 0;
        Node ListPointer = head;                                            // Assigns a Node reference to the list head
        String tempName;
        Llist List1 = new Llist();                                          // creates two lists- list1 and list2, and Merged list
        Llist List2 = new Llist();
        Llist MergedList;
        int halfway = counter/2;                                            // to calculate the middle of the list to be split into half
        while(newCounter != halfway){                                       // while loop to run from starting of the list to the midpoint of the list
            tempName = ListPointer.getName();
            List1.addToList(tempName);                                      // adds data to list1
            ListPointer = ListPointer.getNext();                            // iterates ListPointer to next node
            newCounter++;                                                   // increase to continue the while loop
        }
        while(halfway != counter){                                          // while loop to run from midpoint to the end of the list
            tempName = ListPointer.getName();
            List2.addToList(tempName);                                      // adds data to list2
            ListPointer = ListPointer.getNext();
            halfway++;                                                      // increases half way for the while loop to reach end
        }
        System.out.println("List1-");
        List1.traverse();;                                                  // traverses List1 & List2 and displays contents
        System.out.println("List2-");
        List2.traverse();
        MergedList = List1.merge(List2.head);                               // Merges List1 & List2 and returns a merged list which is now MergedList
        System.out.println("List1 and List2 after merge- ");
        MergedList.traverse();                                              // traverses MergedList and displays contents
    }
    public Llist merge(Node l2){                                            // Method to merge two lists by accepting pointers and merges them into one single list
        Llist NewList = new Llist();
        Node l1 = head;
        while(l1 != null){
            NewList.addToList(l1.getName());
            l1 = l1.getNext();
        }
        while(l2 != null){
            NewList.addToList(l2.getName());
            l2 = l2.getNext();
        }
        return NewList;
    }
}


public class Main {
    static public Llist Readfile(){                                         // Methods to read the input file and insert contents into the list.
        String name;
        Llist list = new Llist();
        try {
            File read = new File("/Users/vibhorsagar/Desktop/input.txt");   // Reads file from destination provided
            Scanner input = new Scanner(new FileReader(read));
            while(input.hasNextLine()){
                name = input.nextLine();
                list.addToList(name);
            }
        }
        catch (FileNotFoundException e){
            System.out.println("File not found");
        }
        return list;
    }

    public static void main(String[] args){                                 // main begin.
        int counter = 0 ;                                                   // Initializing counter
        Llist mainList = Readfile();                                        // Read from file and return List
        System.out.println("The file contains- ");
        mainList.traverse();                                                // Read contents of List
        counter = mainList.GetLength();                                     // Gets the length of the list
        System.out.println("After Split- ");
        mainList.Split_Merge(counter);                                      // Split_Merge method called to split the list
    }
}

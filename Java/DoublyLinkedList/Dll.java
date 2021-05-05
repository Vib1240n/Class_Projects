import java.util.*;
import java.io.*;

class Node {                                                                                                            //  Node class begin
    private String data;
    private Node next;
    private Node prev;

    Node(String data) {                                                                                                 //  Constructor start
        this.data = data;
        next = null;
        prev = null;
    }

    public void setData(String data) {                                                                                  //  setter for data, sets data
        this.data = data;
    }

    public String getData() {                                                                                           //  getter for data, return this.data
        return data;
    }

    public void setNext(Node n) {                                                                                       //  setter for next reference, sets next to n
        this.next = n;
    }

    public void setPrev(Node p){                                                                                        //  setter for previous pointer, sets the prev to p
        this.prev = p;
    }

    public Node getPrev(){                                                                                              //  returns previous pointer of the node
        return prev;
    }

    public Node getNext() {                                                                                             //  getter for next reference, returns this.next
        return next;
    }
}

class DoublyLinkedList{                                                                                                 //  doubly linked list class start
    private Node head;                                                                                                  //  head pointer
    private Node tail;                                                                                                  //  tail pointer
    private int length;                                                                                                 //  length variable for length of the list

    public void push(String data) {                                                                                     //  push method, pushes the word into the list while sorting it correctly
        Node newNode = new Node(data);                                                                                  //  creates new Node

        if (head == null) {                                                                                             //  checks if head is null, if true then puts new node as the head and tail of the list
            head = tail = newNode;
            length++;                                                                                                   //  increments length of the list
        } else if (data.compareTo(tail.getData()) > 0) {                                                                //  checks if the String pushes is lexicographically greater than the tail string of the list, if yes call method pushBack
        newNode = null;                                                                                                 //  makes the node created to null to be deleted by compiler
            pushBack(data);
            length++;
        } else if (data.compareTo(head.getData()) < 0) {                                                                //  checks if the String pushes is lexicographically less than the head string of the list, if yes call method pushFront

            newNode = null;
            pushFront(data);
            length++;
        } else {                                                                                                        //  If the word is less than head, greater than tail, call method pushBetween to push word between nodes
            pushBetween(data);
            length++;
        }
    }
    public void pushFront(String data){                                                                                 //  pushFront method start, pushes the node before the current head of the list
        Node newNode = new Node(data);
        newNode.setNext(head);
        head.setPrev(newNode);
        head = newNode;
    }
    public void pushBack(String data){                                                                                  //  pushBack method start, pushes the node after the current tail of the list
        Node newNode = new Node(data);
        newNode.setPrev(tail);
        tail.setNext(newNode);
        tail = newNode;;
    }
    public void pushBetween(String data){                                                                               //  push between start, pushes the node between two existing nodes
        Node newNode = new Node(data);
        Node curr = head;
        boolean found = false;

        while(curr != tail && found == false){                                                                          //  while loop to loop through the end of the list while word not found to
            if(data.compareTo(curr.getData()) >= 0 && data.compareTo(curr.getNext().getData()) <= 0){                   //  if condition to check if the word is greater than the current node and less than the node after the current node
                newNode.setPrev(curr);
                newNode.setNext(curr.getNext());
                newNode.getNext().setPrev(newNode);
                curr.setNext(newNode);
                found = true;
            }
            else{
                curr = curr.getNext();
            }
        }
    }
    public String popFront(){                                                                                           //  deletes the node at head, increments the head pointer, returns the word being deleted
        String data = head.getData();
        head = head.getNext();
        length--;
        return data;
    }
    public String popBack(){                                                                                            //  deletes the node at tail, decrements the tail pointer, returns the word being deleted
        String data = tail.getData();
        tail = tail.getPrev();
        length--;
        return data;
    }
    public String popAt(String a) {                                                                                     //  deletes the node at specific location by searching for the word through the list, returns the word being deleted
        boolean find = false;
        String temp = a;
        Node curr = head;
        while (curr != null && !find) {                                                                                 //  while loop to loop through the list to search for the word
            if (a.compareTo(curr.getData()) == 0) {
                find = true;
            } else {
                curr = curr.getNext();
            }
        }
        if (find == true ) {                                                                                            //  if statement start when word it found, starts to delete the word
            if (curr.getPrev() == null) {
                popFront();
                System.out.print("Deleted");
            } else {
                curr.getPrev().setNext(curr.getNext());
                System.out.print("Deleted");
            }
            if (curr.getNext() == null) {
                popBack();
                System.out.print("Deleted");
            } else {
                curr.getNext().setPrev(curr.getPrev());
                System.out.print("Deleted");
            }
        }
        return temp;
    }
    public boolean isEmpty(){                                                                                           //  checks if the list if empty, returns true or false
        if (length == 0)
            return true;
        else
            return false;
    }
    public void printFront(){                                                                                           //  prints the list from head to tail
        int i = 1;
        Node curr = head;
        while(curr != null){
            System.out.println(i+ ". "  + curr.getData());
            i++;
            curr = curr.getNext();
        }
    }
    public void printBack(){                                                                                            //  prints the list from tail to head
        int i = length;
        Node curr = tail;
        while(curr != null){
            System.out.println(i+". " + curr.getData());
            i--;
            curr = curr.getPrev();
        }
    }
    public int Length(){                                                                                                //  returns the length of the list
        return length;
    }
}
public class Dll {                                                                                                   //  Driver class start
    public static void main(String[] args) throws IOException {                                                         //  main method start
        File file = new File("/Users/vibhorsagar/Desktop/input.txt");                                                   //  File variable to read the file from given file path
        FileReader reader = new FileReader(file);                                                                       //  FileReader class to help read file
        Scanner input = new Scanner(reader);                                                                            //  Scanner class to take the words in the file as input
        Scanner userInput = new Scanner(System.in);
        DoublyLinkedList list = new DoublyLinkedList();                                                                 //  doublyLinkedList class object
        String deletedWord = "";
        while(input.hasNext()){                                                                                         //  while loop to loop through the file to read in words
            String words = input.next();
            if(words.equals("delete")){                                                                                 //  deletes the words in file with prefix "delete"
                words = input.next();
                deletedWord = list.popAt(words);                                                                        //  list popAt method called to delete word with unknown position
                System.out.println("Word Deleted: "+ deletedWord );                                                     //  displays the word deleted
            }else {
                list.push(words);                                                                                       //  else pushes the word into the list
            }
        }
        System.out.println("Size of list: " + list.Length());                                                           //  prints the size of the list with all the words
        list.printFront();                                                                                              //  prints the list with method printFront
        System.out.println("\n");
        list.printBack();                                                                                               //  prints the list with method printBack
        userInput.close();                                                                                              //  Scanner class close
        input.close();                                                                                                  //  Scanner class close
        reader.close();                                                                                                 //  reader class close
    }
}

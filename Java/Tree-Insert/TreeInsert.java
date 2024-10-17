import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;
import java.io.File;

class Node{                                                                                                             //  Node class start
    private int data;                                                                                                   //  data for the node
    private Node left;                                                                                                  //  Left pointer for the code
    private Node right;                                                                                                 //  right pointer for the code
    Node(int data){                                                                                                     //  Node class constructor
        this.data = data;
        this.left = this.right = null;
    }
    public void setData(int data){                                                                                      //  sets data of the Node
        this.data = data;
    }
    public void setLeft(Node l){                                                                                        //  Sets left of the Node
        this.left = l;
    }
    public void setRight(Node r){                                                                                       //  Sets right of the node
        this.right = r;
    }
    public int getData(){                                                                                               //  Returns the data of the node
        return data;
    }
    public Node getLeft(){                                                                                              //  Returns left of the Node
        return this.left;
    }
    public Node getRight(){                                                                                             //  Returns right of the Node
        return this.right;
    }
}

class  Tree {                                                                                                           //  Tree class begin
    private Node root = null;                                                                                           //  Root Node of tree is null

    public void push(int data){                                                                                         //  Puh method of the tree
        root = insert(root, data);                                                                                      //  Recursively calls insert method
    }
    public void pop(int data){                                                                                          //  Pop method of the tree
        root =  delete(root, data);                                                                                     //  Recursively calls delete method
    }
    public void print(){                                                                                                //  Print method of the tree
        System.out.print("InOrder Traversal:    ");
        inOrder(root);                                                                                                  //  calls inOrder method
        System.out.print("\nPostOrder Traversal:  ");
        postOrder(root);                                                                                                //  calls postOrder method
        System.out.print("\nPreOrder Traversal:   ");
        preOrder(root);                                                                                                 //  calls preOrder method
    }

    public Node insert(Node leaf, int data){                                                                            //  Insert method of the tree
        if(leaf == null){
            leaf = new Node(data);
            return leaf;
        }
        if(data < leaf.getData()){
            leaf.setLeft(insert(leaf.getLeft(), data));
        }else if(data > leaf.getData()){
            leaf.setRight(insert(leaf.getRight(), data));
        }
        return leaf;
    }
    public Node delete(Node leaf, int data){                                                                            //  Delete method of the tree
        if(leaf == null){
            return null;
        }
        if(data < leaf.getData()){
            leaf.setLeft(delete(leaf.getLeft(), data));
        }else if(data > leaf.getData()){
            leaf.setRight(delete(leaf.getRight(), data));
        }else{
            if(leaf.getLeft() == null){
                return leaf.getRight();
            }else if(leaf.getRight() == null) {
                return leaf.getLeft();
            }
            leaf.setData(minValueInTreeBranch(leaf.getRight()));
            leaf.setRight(delete(leaf.getRight(), leaf.getData()));
        }
        return leaf;
    }
    public int minValueInTreeBranch(Node leaf){                                                                         //  Returns the min value in the tree branch
        int temp = leaf.getData();
        while(leaf.getLeft() != null){
            temp = leaf.getLeft().getData();
            leaf = leaf.getLeft();
        }
        return temp;
    }
    public void preOrder(Node leaf)                                                                                     //  Prints the tree in pre Order method
    {
        if(leaf != null)
        {
            System.out.print(leaf.getData());
            preOrder(leaf.getLeft());
            preOrder(leaf.getRight());
        }
    }
    public void inOrder(Node leaf)                                                                                      //  Prints tree in InOrder method
    {
        if(leaf != null)
        {
            inOrder (leaf.getLeft());
            System.out.print(leaf.getData());
            inOrder (leaf.getRight());
        }
    }
    public void postOrder(Node leaf)                                                                                    //  Prints tree in Post Order method
    {
        if(leaf != null)
        {
            postOrder(leaf.getLeft());
            postOrder (leaf.getRight());
            System.out.print(leaf.getData());
        }
    }
}

public class TreeInsert {
    static Tree tree = new Tree();                                                                                      //  Global tree object in class

    public static void readFromFile(String name) throws FileNotFoundException {
        File file = new File(name);                                                   //  File variable to read the file from given file path
        FileReader reader = new FileReader(file);                                                                       //  FileReader class to help read file
        Scanner input = new Scanner(reader);                                                                            //  Scanner class to take the words in the file as input;
        int data;
        int deleted;
        while(input.hasNext()){                                                                                         //  while loop to loop through the file to read in words
            String words = input.next();
            if(words.equals("delete")){                                                                                 //  deletes the words in file with prefix "delete"
                words = input.next();
                data = Integer.parseInt(words);
                tree.pop(data);                                                                                         //  list popAt method called to delete word with unknown position
                deleted = data;
                System.out.println("Value Deleted: "+ deleted );                                                        //  displays the word deleted
            }else {
                data = Integer.parseInt(words);
                tree.push(data);                                                                                        //  else pushes the word into the list
            }
        }
        input.close();

    }
    public static void main(String[] args) throws FileNotFoundException {                                               //  Main method begin
        String FileName;
        Scanner input = new Scanner(System.in);
        System.out.print("Enter File path name: ");
        FileName = input.nextLine();
        readFromFile(FileName);                                                                                                 //  Read from file method called
        tree.print();
        input.close();                                                                                                   //  tree print method called
    }
}

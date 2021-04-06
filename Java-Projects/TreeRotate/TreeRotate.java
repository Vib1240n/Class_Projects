import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

class Node {
    private int data; // Node Data
    private int Height; // Node Height
    private Node left; // Node left pointer
    private Node right; // Node right pointer

    Node(int data) { // Node constructor to set data and height
        this.data = data;
        this.Height = 1;
    }

    public void setData(int data) { // sets data of the Node
        this.data = data;
    }

    public void setLeft(Node l) { // Sets left of the Node
        this.left = l;
    }

    public void setRight(Node r) { // Sets right of the node
        this.right = r;
    }

    public int getData() { // Returns the data of the node
        return data;
    }

    public Node getLeft() { // Returns left of the Node
        return this.left;
    }

    public Node getRight() { // Returns right of the Node
        return this.right;
    }

    public int getHeight() { // Returns the height of the Node
        return this.Height;
    }

    public void setHeight(int Height) { // sets the height of the Node
        this.Height = Height;
    }
}

class Tree {
    private Node root = null; // Root of the tree

    public void push(int data) { // Method to populate the tree
        root = insert(root, data);
    }

    public Node insert(Node leaf, int data) { // Method to populate the tree using recurrsion
        if (leaf == null) {
            leaf = new Node(data);
            return leaf;
        } else if (data < leaf.getData()) {
            leaf.setLeft(insert(leaf.getLeft(), data));
        } else if (data > leaf.getData()) {
            leaf.setRight(insert(leaf.getRight(), data));
        }
        leaf = rebalance(leaf, data); // Rebalances the tree after each insert of Node
        return leaf;
    }

    int Height(Node n) { // Returns height of the node
        if (n == null)
            return 0;
        return n.getHeight();
    }

    int getBalance(Node n) { // Method to get balance of the left and right Node and return it
        if (n == null) {
            return 0;
        }
        int balance = Height(n.getLeft()) - Height(n.getRight());
        return balance;
    }

    public Node rebalance(Node leaf, int data) { // Rebalances the tree using rotation of the Nodes
        leaf.setHeight(Math.max(Height(leaf.getLeft()), Height(leaf.getRight())) + 1);

        int bal = getBalance(leaf);

        if (bal > 1 && data < leaf.getLeft().getData()) {
            return RotateRight(leaf);
        }
        if (bal < -1 && data > leaf.getRight().getData()) {
            return RotateLeft(leaf);
        }
        if (bal > 1 && data > leaf.getRight().getData()) {
            leaf.setLeft(RotateLeft(leaf.getLeft()));
            ;
            return RotateRight(leaf);
        }
        if (bal < -1 && data < leaf.getRight().getData()) {
            leaf.setRight(RotateRight(leaf.getRight()));
            ;
            return RotateLeft(leaf);
        }
        return leaf;
    }

    public Node RotateRight(Node leafNode) { // Rotates the Node to the right
        Node rightNode = leafNode.getLeft();
        Node leftNode = rightNode.getRight();
        leafNode.setLeft(leftNode);
        rightNode.setRight(leafNode);
        leafNode.setHeight(Math.max(Height(leafNode.getLeft()), Height(leafNode.getRight())) + 1);
        rightNode.setHeight(Math.max(Height(rightNode.getLeft()), Height(rightNode.getRight())) + 1);
        return rightNode;
    }

    public Node RotateLeft(Node leafNode) { // Rotates the Node to the left
        Node rightNode = leafNode.getRight();
        Node leftNode = rightNode.getLeft();
        leafNode.setRight(leftNode);
        rightNode.setLeft(leafNode);
        rightNode.setHeight(Math.max(Height(rightNode.getLeft()), Height(rightNode.getRight())) + 1);
        leafNode.setHeight(Math.max(Height(leafNode.getLeft()), Height(leafNode.getRight())) + 1);
        return rightNode;
    }

    int Depth(Node n) { // Returns the Depth of the Node in tree
        if (n == null)
            return 0;
        else {
            int leftDepth = Depth(n.getLeft());
            int rightDepth = Depth(n.getRight());
            if (leftDepth > rightDepth)
                return (leftDepth + 1);
            else
                return (rightDepth + 1);
        }
    }

    public Node getRoot() { // Returns the root Node of the tree
        return this.root;
    }
}

public class TreeRotate
 { // Driver class Begin
    static Tree tree = new Tree(); // Global Tree class object
    static ArrayList<Integer> output = new ArrayList<Integer>(); // Global arraylist to store tree->node->data
    static String fileName = "output.txt"; // Output file name

    public static void ReadFromFile() throws FileNotFoundException { // Read from file method reads from a txt file
        File file = new File("input.txt");
        FileReader reader = new FileReader(file);
        Scanner input = new Scanner(reader);
        while (input.hasNext()) {
            String words = input.next();
            tree.push(Integer.parseInt(words));
        }
        input.close();
    }

    public static void printLevel(Node root, int level) throws IOException { // Print level method, prints level of the
                                                                             // tree
        if (root == null) {
            return;
        }
        if (level == 1) {
            int data = root.getData();
            output.add(data);
        } else if (level > 1) {
            printLevel(root.getLeft(), level - 1);
            printLevel(root.getRight(), level - 1);
        }
    }

    public static void printLevelOrder() throws IOException { // print level order method
        int Height = tree.Depth(tree.getRoot());
        for (int i = 1; i <= Height; i++) {
            printLevel(tree.getRoot(), i);
            System.out.println();
        }
    }

    static public void WrtieToFile(ArrayList<Integer> output) throws IOException { // Write to file method write output
                                                                                   // in txt file
        if (fileName.length() != 0) {
            FileWriter fwOb = new FileWriter(fileName, false);
            PrintWriter pwOb = new PrintWriter(fwOb, false);
            pwOb.flush();
            pwOb.close();
            fwOb.close();
            System.out.println("File Cleared for new output");
        }
        File outFile = new File(fileName);
        FileWriter writeFile = new FileWriter(outFile, true);
        BufferedWriter buffer = new BufferedWriter(writeFile);
        for (int j = 0; j < output.size(); j++) {
            buffer.write(output.get(j) + " | ");
        }
        buffer.newLine();
        buffer.write("Name: Vibhore Sagar");
        buffer.write("\n      CSC-130");
        buffer.close();
    }

    public static void main(String[] args) throws Exception { // main method start
        ReadFromFile();
        printLevelOrder();
        WrtieToFile(output);
    }
}

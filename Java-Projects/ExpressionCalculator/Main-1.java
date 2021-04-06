package com.company;
import java.util.*;


class Node<T>{                                                                                                          // Generic Node class begin
    private T data;
    private Node<T> next;
    Node(T data){                                                                                                       //  Constructor start
        this.data = data;
        next = null;
    }
    public void setData(T data){                                                                                        //  setter for data, sets data
        this.data = data;
    }
    public T getData(){                                                                                                 //  getter for data, return this.data
        return data;
    }
    public void setNext(Node<T> n){                                                                                     //  setter for next reference, sets next to n
        this.next = n;
    }
    public Node<T> getNext(){                                                                                           //  getter for next reference, returns this.next
        return next;
    }
}

class Stack<T>{                                                                                                         //  Generic class stack begin
    private Node<T> top = null;                                                                                         //  Node reference for Stack top
    int length = 0;
    public void push(T data) {                                                                                          //  push method, to push data in stack
        Node<T> newNode = new Node<T>(data);
        newNode.setNext(top);                                                                                           //  sets newNode to top
        top = newNode;
        length++;
    }
    public boolean isEmpty(){                                                                                           //  isEmpty method to check is stack is empty
        if(top == null){
            return true;                                                                                                //  returns true if stack is empty
        }
        else{
            return false;                                                                                               //  returns false if stack not empty
        }
    }
    public T peek(){                                                                                                    //  peek method to check the top value in stack
        T value = null;
        if(isEmpty()){
            return value;                                                                                               //  if stack is empty returns -1
        }else{
            return top.getData();                                                                                       //  else returns top data in stack
        }
    }
    public T pop(){                                                                                                     //  pop method to pop top value from stack
        T value = null;
        if(isEmpty()){
            return value;                                                                                               //  returns null if the Stack is empty
        }else{
            T temp = top.getData();                                                                                     //  gets value that is being popped
            top = top.getNext();                                                                                        //  increments top pointer
            length--;                                                                                                   //  decreases length of Stack
            return temp;                                                                                                //  returns the popped value
        }
    }
    public void print(){                                                                                                //  print method to print stack elements
        Node<T> curr = top;
        if(isEmpty()){
            System.out.println("Stack Empty");
        }else{
            while(curr != null){
                System.out.println(curr.getData());
                curr = curr.getNext();
            }
        }
    }
    public int Length(){                                                                                                //  length method to return number of elements in the stack
        return length;
    }
    public Node<T> getTop() {                                                                                           //  Returns top pointer of the Stack
            return top;
        }
}

class Queue<T>{                                                                                                         //  Queue class begin
    private Node<T> front = null;                                                                                       //  Node reference for front of the queue
    private Node<T> back = null;                                                                                        //  Node reference for back of the queue
    int length = 0;                                                                                                     // initial length of the queue

    public void enqueue(T data){                                                                                        //  enqueue method to insert values in the queue
        Node<T> newNode = new Node<T>(data);
        if (back == null) {                                                                                             //  if the front is null then newNode is front and back
            front = newNode;
            back  = newNode;
            length++;
        }
        back.setNext(newNode);                                                                                          //  else sets the newNode at the back of the queue
        back = newNode;
        length++;                                                                                                       //  increments length of the queue by 1
    }
    public T dequeue(){                                                                                                 //  dequeue method start
        Node<T> curr = front;
        front = front.getNext();                                                                                        //  sets front to the value right after current front
        return curr.getData();                                                                                          //  returns current front value
    }
    public Node<T> getFront(){                                                                                          //  returns the front pointer of the queue
        return front;
    }
    public Node<T> getBack(){                                                                                           //  returns the back pointer of the queue
        return back;
    }
    public int Length(){                                                                                                //  returns the length of the queue
        return length;
    }
    public boolean isEmpty(){                                                                                           //  isEmpty boolean method to return true or false if the queue is empty or not
        if(front == null){
            return true;
        }
        else{
            return false;
        }
    }
    public void print(){                                                                                                //  prints out all the elements in the queue
        Node curr = front;
        if(isEmpty()){
            System.out.println("Stack Empty");
        }else{
            while(curr != null){
                System.out.println(curr.getData());
                curr = curr.getNext();
            }
        }
    }
}

class ExpressionCalculator {                                                                                            //  Expression Calculator class begin
    private Stack<Integer> numStack = new Stack<>();                                                                    //  numStack variable initialized
    private Queue<Character> postFixQ  = new Queue<>();                                                                 //  postFixQ variable initialized
    private Stack<Integer> Evaluate = new Stack<>();                                                                    //  Evaluate variable initialized
    public boolean is_digit(char token)                                                                                 //  is_digit boolean method begin- checks if the character is a digit or not
    {
        char []s = {'1','2','3','4','5','6','7','8','9','0'};
        for(int i = 0; i< 10; i++){
            if(token == s[i]){
                return true;
            }
        }
        return false;
    }
    public int precedence(char op)                                                                                      //  precedence method start- returns the precedence value based on the operator
    {
        if (op == '+' || op == '-') { return 1; }
        else if (op == '*' || op == '/') { return 2; }
        else { return 0; }
    }
    public void EvauateQueue(){                                                                                         //  Evaluates the postfix expression in queue and pushes result into a stack
        int final_result = 0;
        int num1 =0 , num2 = 0;
        char c= ' ';
        Node<Character> curr = postFixQ.getFront();                                                                     //  curr pointer for the front of the queue
        while(curr != null){                                                                                            //  while loop to iterate through the whole queue
            c = curr.getData();
            if(is_digit(c)){                                                                                            //  checks if queue value is digit or not
                Evaluate.push(Character.getNumericValue(c));                                                            //  if its a digit then pushes into the stack
            }else {                                                                                                     //  else pops the most recent 2 values from the stack to evaluate
                num1 = Evaluate.pop();
                num2 = Evaluate.pop();
                switch(c){                                                                                              //  switch-case to see which operator is queue value
                    case '+' :
                        int temp = num2+num1;
                        Evaluate.push(temp);
                        break;
                    case '-' :
                        temp = num2-num1;
                        Evaluate.push(temp);
                        break;
                    case '*' :
                        temp = num2*num1;
                        Evaluate.push(temp);
                        break;
                    case '/' :
                        temp = num2/num1;
                        Evaluate.push(temp);
                        break;
                    default:
                        System.out.println("Error 4");                                                                  //  shows error
                }
            }
            curr = curr.getNext();                                                                                      //  increments the curr pointer to next node in queue
        }
    }
    public String Expression_Calculator (String expression) {                                                           //  Expression_Calculator method start- converts from infix to postfix expression and calls EvaluateStack method
        String result = new String("");
        char c = ' ';
        for(int i=0; i<expression.length(); i++)                                                                        //  for loop to run throught the whole string
        {
            c = expression.charAt(i);
            if(is_digit(c))                                                                                             //  to check if string at i is digit or not
            {
                postFixQ.enqueue(c);                                                                                    //  if digit pushes into the postFixQ queue
            }
            else if(c == '(')                                                                                           //  checks if the string value is "("
            {
                numStack.push((int)c);
            }
            else if(c == ')' )                                                                                          //  checks if the string value is ")"
            {
                while(numStack.getTop()!=null && numStack.peek()!='(')                                                  //  checks if the top is null and top value in stack
                {
                    int temp = numStack.pop();                                                                          //  pops the top value of stack
                    char r = (char)temp;
                    postFixQ.enqueue(r);                                                                                //  pushes into the queue
                }
                if(numStack.getTop()==null)                                                                             //  if top of stack is null
                {
                    return "Error 1";                                                                                   //  returns error
                }
                else numStack.pop();
            }
            else
            {
                int t = numStack.getTop().getData();
                char T = (char)t;
                while(numStack.getTop() != null && precedence(c) < precedence(T))                                       //  if string value is operator then checks if the precedence between top and value
                {
                    if(numStack.getTop().getData() == '(')                                                              //  if top is "(" throws error 2
                        return "Error 2";
                    postFixQ.enqueue((char)((int)numStack.pop()));                                                      //  else pushes string value in queue
                }
                numStack.push((int)c);
            }
        }
        while(numStack.getTop() != null)
        {
            if(numStack.getTop().getData() == '(')
                return "Error 3";
            postFixQ.enqueue((char)((int)numStack.pop()));
        }
        EvauateQueue();                                                                                                 //  calls Evaluate queue method to evaluate queue
        Node<Character> curr = postFixQ.getFront();
        while(curr != null){
            char ch = curr.getData();
            result += ch;                                                                                               //  converts the postfix expression into string
            curr = curr.getNext();
        }
        return result;
    }
    public Stack<Integer> return_numStack(){                                                                            //  returns numStack
        return numStack;
    }
    public Queue<Character> return_PostFixQ(){                                                                          //  returns PostFixQ
        return postFixQ;
    }
    public Stack<Integer> return_EvaluateQueue(){                                                                       //  returns evalStack
        return Evaluate;
    }
}
public class Main {                                                                                                     //  main class start
    public static void main(String[] args) {                                                                            //  main method start
        String postFix;                                                                                                 //  Data variable to accept the post fix value
        String temp;
        ExpressionCalculator calculator = new ExpressionCalculator();                                                   //  Instance of ExpressionCalculator class
        Scanner input = new Scanner(System.in);                                                                         //  Scanner class open
        System.out.println("Enter InFix expression{ eg: ((1+2)-(3+4)*5)  }");
        postFix = input.nextLine();                                                                                     //  Get input from user
        temp = calculator.Expression_Calculator(postFix);                                                               //  Expression_Calculator called to evaluate postfix expression
        System.out.println("PostFix Expression: "+temp);
        int result = calculator.return_EvaluateQueue().pop();                                                           //  pop the stack and get the final result of the expression
        System.out.println("="+result);                                                                                 //  Display the result
        input.close();                                                                                                  //  Scanner class close

    }
}

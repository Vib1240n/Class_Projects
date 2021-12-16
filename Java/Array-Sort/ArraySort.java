import java.util.Scanner;
/*
Vibhore Sagar
CS-130
 */

class SortSearch{                                                                                                       //Sort-Search class start
    void Bubble_sort(int[][] array, int row, int col){                                                                  //  bubble sort method, takes in 2d array and sorts it using bubble sort
        int constant = 0;
        int j =0;
        while(j < 1 ) {
            for (int i = 0; i < array.length; i++) {
                
                for (int k = 0; k < array.length-i-1; k++) {
                    if (array[k][constant] > array[k+1][constant]) {
                        int temp = array[k][constant];
                        array[k][constant] = array[k + 1][constant];
                        array[k + 1][constant] = temp;
                    }

                }
            }
            j++;
        }
        printArray(array,row,col);                                                                                      //  Prints the array after sorting
    }

    void binary_search(int[][] array, int row, int col, int numToSearch){                                               //  Binary search method, search for the number in the 5th col of the 2d array and displays it
        int mid = 0;
        int low = 0;
        int high = col - 1;
        boolean found = false;

        while (high >= low && !found) {
            mid = (high + low) / 2;
            if (array[row-1][mid] < numToSearch) {
                low = mid + 1;
            }
            else if (array[row-1][mid] > numToSearch) {
                high = mid - 1;
            }
            else {
                found = true;
            }
        }
        if( found == true){
            System.out.println("Number found in col");
            for(int i = 0; i < row; i++){
                System.out.println(array[i][mid]);
            }
        }
        else{
            System.out.println("Not Found:"+ numToSearch);
        }
    }
    void inserstion_sort(int[][] array, int row, int col){                                                              //  Insertion sort method, performs insertion sort on the last row of the 2d array
        int temp = 0;
        int rts = row-1;
        for(int i = 1; i < rts; i++){
            for( int k = i; k >0 && array[rts][k-1] > array[rts][k]; k--){
                for(int j = 0; j < row; j ++){
                    temp = array[j][k];
                    array[j][k] = array[j][k-1];
                    array[j][k-1]= temp;
                }
            }
        }
        printArray(array,row,col);                                                                                      //  prints array after sort
    }
    void shell_sort(int array[][], int row, int col){                                                                   //  Shell sort method, sorts 3rd col of the 2d arary
        int temp = 0;
        int j = 2;
        for(int gap = row/2; gap >= 1; gap = gap/2 ){
            for(int i = gap; i< row; i++){
                for( int k = i; k >=gap && array[k-gap][j]> array[k][j];  k = k -gap){
                    temp = array[k-gap][j];
                    array[k-gap][j] = array[k][j];
                    array[k][j] = temp;
                }
            }
        }
        printArray(array, row, col);                                                                                    //  prints array after sort
    }
    void selection_sort(int[][] array, int row, int col) {                                                              //  Selecton sort method, sorts 2nd col of 2d array
        int limit = row - 1;
        int constant = 1;
        int indexLargest = 0;
        int temp = 0;  // Temporary variable for swap

        for (; limit > 0; limit--) {
            indexLargest = 0;
            for (int i = 1; i <= limit; i++) {
                if (array[i][constant] < array[indexLargest][constant]) {
                    indexLargest = i;
                }
            }
            if (limit != indexLargest) {
                for (int k = 0; k < row - 1; k++) {
                    temp = array[limit][k];
                    array[limit][k] = array[indexLargest][k];
                    array[indexLargest][k] = temp;
                }
            }
        }
        printArray(array, row, col);                                                                                    //  prints array after sort
    }
    void printArray(int array[][], int row, int col){                                                                   //  Prints array method, prints array when called
        for( int i = 0; i< row; i ++){
            for(int j = 0 ; j < col ; j ++){
                System.out.print(array[i][j]+ " ");
            }
            System.out.println("\n");
        }
    }
}


public class ArraySort {                                                                                                   //  Driver class start
    final static int row = 5;                                                                                           //  Const row size declared
    final static int col = 4;                                                                                           //  Const col size declared
    final static int[][] array = {{5,3,2,16},                                                                           //  Const 2d arrat declared
                                  {9,8,10,17},
                                  {4,7,11,18},
                                  {2,5,9,12},
                                  {7,9,4,10}
    };

    static int[][] reset(int[][] TempArray){                                                                            //  Reset method, resets 2d array to original array when called
        for(int i = 0;  i< row; i ++){
           for(int j =0; j <col; j++){
               TempArray[i][j] = array[i][j];
           }
       }
        return TempArray;                                                                                               //  Returns reset array
    }

    public static void main(String[] args){                                                                             //  Main method start

        SortSearch ss = new SortSearch();                                                                               //  Sort search class objects
        Scanner input = new Scanner(System.in);                                                                         //  Scanner class object

        int[][] tempArray = new int[row][col];                                                                          //  Temp array created

        tempArray = reset(tempArray);                                                                                   //  get original array from reset method
        System.out.println("Array before any sort");
        ss.printArray(tempArray,row,col);

        System.out.println("bubble Sort");
        ss.Bubble_sort(tempArray, row, col);                                                                            //  Bubble sort method called
        tempArray = reset(tempArray);                                                                                   //  Array reset

        System.out.println("\n" + "Selection sort");
        ss.selection_sort(tempArray, row,col);                                                                          //  Selection sort method called
        tempArray = reset(tempArray);                                                                                   //  Array reset

        System.out.println("\n" + "Shell sort");                                                                        //  Shell sort method caled
        ss.shell_sort(tempArray, row,col);
        tempArray = reset(tempArray);                                                                                   //array reset

        System.out.println("\n" + "Insertion sort");                                                                    //  Insertion sort method called
        ss.inserstion_sort(tempArray, row, col);

        System.out.println("Enter number to search in 5th row:");                                                       //  Asks user to enter number for search
        int search_num = input.nextInt();                                                                               //  Take input
        ss.binary_search(tempArray,row,col,search_num);                                                                 //  Search for number using binary search method

        input.close();


    }
}

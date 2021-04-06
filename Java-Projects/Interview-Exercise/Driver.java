import java.util.Scanner;

public class Driver {

    static int max(int[] arr) { // To calculate max in array and return index
        int index = 0;
        int max = arr[0];
        for (int a = 0; a < arr.length; a++) { // For loop to find the largest number in array to use as pivot
            if (arr[a] > max) {
                max = arr[a];
                index = a;
            }
        }
        return index;
    }

    static boolean isValidMountainArray(int[] arr) { // To find out whether an array is a mountain
        boolean valid = false; // bool variable to see if array is valid mountain
        if (arr.length < 3) { // checks to see if array can be a mountain or not
            return false;
        }
        int k = max(arr); // index for the maximum number in array
        if (k == arr.length - 1 || k == 0) { // checks if the pivot is at the beginning or at end
            return false;
        }
        for (int index = 0; index < k; index++) { // runs loop from 0 to pivot and checks if its strictly increasing
            if (arr[index] < arr[index + 1]) {
                valid = true;
            } else {
                return false;
            }
        }
        for (int index = arr.length - 1; index > k; index--) { // runs loop from end of array till pivot and checks if
                                                               // its strictly increasing
            if (arr[index] < arr[index - 1]) {
                valid = true;
            } else {
                return false;
            }
        }
        return valid;
    }

    static int LongestMountainArray(int[] arr) { // To calculate longest mountain subarray in array
        int longest = 0;
        int ans = 0;
        int i = 1;
        while (i < arr.length) { // runs for loop from 1 to array length
            if (arr[i] > arr[i - 1]) { // checks if its increasing slope
                longest++;
                i++;
            } else if (longest == 0 && arr[i] <= arr[i - 1]) { // checks if loop starts from downwards slope
                i++;
            } else if (longest != 0 && arr[i] == arr[i - 1]) { // checks if upwards slope turns into plane
                longest = 0;
                i++;
            }
            // going down hill
            else if (longest != 0 && arr[i - 1] > arr[i]) { // checks if slope is going downwards
                while (i < arr.length && arr[i] < arr[i - 1]) { // while loop to check if its strictly decreasing
                    longest++;
                    i++;
                }
                ans = Math.max(ans, longest);
                longest = 0;
            }
        }
        return ans != 0 ? ans + 1 : 0;
    }

    // main function start
    public static void main(String[] argv) {
        boolean isValid;
        int longest;
        String line;
        String[] n = {};
        int[] arr = {};
        int i = 0;
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a set of numbers");
        line = input.nextLine(); // Take set of numbers input as a string
        n = line.split("[\\s,]+");
        arr = new int[n.length]; // initialize array with string length
        while (i != n.length) {
            arr[i] = Integer.parseInt(n[i]); // convert string to array
            i++;
        }
        System.out.println("\n");
        isValid = isValidMountainArray(arr); // pass in array to check validity
        System.out.println("Is valid mountain: " + isValid);
        System.out.println("Enter a set of numbers");
        line = input.nextLine();
        n = line.split("[\\s,]+");
        arr = new int[n.length];
        i = 0;
        while (i != n.length) {
            arr[i] = Integer.parseInt(n[i]);
            i++;
        }
        longest = LongestMountainArray(arr);
        System.out.println("Longest mountain in arr: " + longest);
        input.close();

    }
}
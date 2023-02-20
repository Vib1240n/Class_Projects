
import java.util.*;
import java.lang.*;
import java.io.*;

/*
 * matrix, represents the elements of the matrix of size N*M.
 */
public class Solution {
	public static void funcMatrix(int[][] matrix) {
		// Write your code here
		int rows = matrix.length;
		int cols = matrix[0].length;
		int min_value = Integer.MAX_VALUE;
		int max = 0;
		int min = 0;
		System.out.println("Check 1");
		for (int i = 0; i < rows; i++) {
			int max_value = Integer.MIN_VALUE;
			for (int j = 0; j < cols; j++) {
				max_value = Math.max(max_value, matrix[i][j]);
			}
			min_value = Math.min(min_value, max_value);
		}
		System.out.println("Check 2");
		max = min_value;

		for (int i = 0; i < cols; i++) {
			int max_value = Integer.MIN_VALUE;
			for (int j = 0; j < rows; j++) {
				max_value = Math.max(max_value, matrix[j][i]);
			}
			min_value = Math.min(min_value, max_value);
		}

		min = min_value;
		System.out.println(max);
		System.out.println(min);

	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		// input for matrix
		int matrix_row = in.nextInt();
		int matrix_col = in.nextInt();
		int matrix[][] = new int[matrix_row][matrix_col];
		for (int idx = 0; idx < matrix_row; idx++) {
			for (int jdx = 0; jdx < matrix_col; jdx++) {
				matrix[idx][jdx] = in.nextInt();
			}
		}

		funcMatrix(matrix);

		Scanner sc = new Scanner(System.in);
		StringBuffer s = new StringBuffer();
		String patternstring = "\\(((\\+|-)?((([0-9]|[1-8][0-9])(\\.\\d+)?)|90(\\.0+)?)), ((\\+|-)?((([0-9]|[1-9][0-9]|1[0-7][0-9])(\\.\\d+)?)|180(\\.0+)?))\\)";
		Pattern p = Pattern.compile(patternstring);
		int numOfLines = 0;
		if (sc.hasNextLine()) {
			numOfLines = Integer.valueOf(sc.nextLine());
		}
		while (numOfLines > 0) {
			if (!sc.hasNextLine())
				break;
			String line = sc.nextLine();
			Matcher m = p.matcher(line);
			if (m.find()) {
				System.out.println("Valid");
			} else {
				System.out.println("Invalid");
			}
			numOfLines--;
		}
	}
}
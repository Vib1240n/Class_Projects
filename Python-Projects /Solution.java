import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {

    /*
     * Complete the 'maxPairs' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY skillLevel
     *  2. INTEGER minDiff
     */

    public static int maxPairs(List<Integer> skillLevel, int minDiff) {
    // Write your code here
        int result = 0;
        /*
            1 2 3 4 5 6
            mindiff = 2
            n = 6;
            check 1-2 x
            1-3 n
            1-4 n
            1-5 n
            1-6 n

        */

        int max =0;
        for( int i =0; i < skillLevel;.size(); i ++){
            if(skillLevel.get(i) > max){
                max = skillLevel.get(i);
            }
        }
        if( minDiff > max){
            result = 0;
        }else{
            //find mindiff in skill rank 
            Collections.sort(skillLevel);
            int arr[] = new int[skillLevel.size()];
            for(int i =0; i < skillLevel.size(); i++){
                arr[i] = skillLevel.get(i);
            }
            for(int i = arr.length; i> 0; i--){
                for(int j = i -1; j >0; j--){
                    if(arr[i] - arr[j] >= minDiff){
                        result++;
                    }
                }
            }
            }
        }


        return result; 
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int skillLevelCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> skillLevel = IntStream.range(0, skillLevelCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        int minDiff = Integer.parseInt(bufferedReader.readLine().trim());

        int result = Result.maxPairs(skillLevel, minDiff);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}public class Solution {
    
}

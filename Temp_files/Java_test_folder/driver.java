import java.util.*;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;

public class driver{
    public static void main(String[] args) throws  IOException {
        File file = new File("test.txt");
        FileOutputStream out = new FileOutputStream(file);
        PrintWriter print = new PrintWriter(out);
        System.out.println("Hello");
        String name;
        ArrayList<Integer> arr = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        System.out.print("Enter Name: ");
        name = in.nextLine();
        System.out.println(name);
        in.close();
        for(int i =0; i < 11; i++){
            arr.add(i+1);
            System.out.print(arr.get(i));
            print.print(arr.get(i) + " ");
        }
        print.close();
    }
}
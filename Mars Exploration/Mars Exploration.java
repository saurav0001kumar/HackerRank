import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the marsExploration function below.
    static int marsExploration(String s) {
int len;
len=s.length();
int n=len/3;
int mis=0;
for(int i=0; i<=len-3; i+=3)
{

    if(s.charAt(i)!='S')
    mis+=1;

    if(s.charAt(i+1)!='O')
    mis+=1;

    if(s.charAt(i+2)!='S')
    mis+=1;
    
    
    }
    return(mis);


    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scanner.nextLine();

        int result = marsExploration(s);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}

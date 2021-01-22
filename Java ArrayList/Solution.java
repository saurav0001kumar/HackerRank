import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        
        ArrayList<ArrayList<Integer>> a = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> t = new ArrayList<Integer>();
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        sc.nextLine();
        for (int k = 0; k < n; k++) {
            Scanner s = new Scanner(sc.nextLine());
            while (s.hasNextInt()) {
                t.add(s.nextInt());
            }
            s.close();
            a.add((ArrayList<Integer>) t.clone());
            t.clear();
        }
        int m = sc.nextInt();
        sc.nextLine();
        int i, j;
        for (int k = 0; k < m; k++) {
            i = sc.nextInt() - 1;
            j = sc.nextInt();
            if (i < n && j < a.get(i).size()) {
                System.out.println(a.get(i).get(j));
            }
            else
                System.out.println("ERROR!");
        
        }
    }
}
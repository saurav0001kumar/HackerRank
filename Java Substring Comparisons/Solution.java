import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "",min;
        int j1=0;
        String[] a=new String[s.length()-k+1];
        for(int i=0; i<=s.length()-k; i++)
        {
            String t=""+s.charAt(i)+s.charAt(i+1)+s.charAt(i+2);
            a[i]=t;
        }

        for(int i=0; i<a.length; i++)
        {
            min=a[i];
            for(int j=i; j<a.length; j++)
            {
                if(min.compareTo(a[j])>0)
                {
                    min=a[j];
                    j1=j;
                }
            }
            a[j1]=a[i];
            a[i]=min;
        }
smallest=a[0];
largest=a[a.length-1];
        return smallest + "\n" + largest;
    }

  public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}


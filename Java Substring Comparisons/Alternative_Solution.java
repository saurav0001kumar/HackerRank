import java.util.Scanner;

public class Alternative_Solution {

    public static String getSmallestAndLargest(String s, int k) {
               String smallest = "";
        String largest = "";
        String[] a=new String[s.length()+1-k];
        int c=0;
        char[] c1,c2=new char[k];
        for(int i=0; i<s.length()-k+1; i++)
        {
            String t="";
            for(int j=0; j<k; j++)
            {
                t+=s.charAt(i+j);
            }
            a[c++]=t;
        }
        
        c1=a[0].toCharArray();
        c2=a[0].toCharArray();
        
        for(int i=0; i<a.length; i++)
        {
            for(int j=0; j<k; j++)
            {
                if(a[i].charAt(j)<c1[j])
                {
                    c1=a[i].toCharArray();
                    break;
                }
                else
                    if(a[i].charAt(j)==c1[j])
                        continue;
                    else
                        if(a[i].charAt(j)>c1[j])
                            break;
                        
            }
  
        }

        
        for(int i=0; i<a.length; i++)
        {
            for(int j=0; j<k; j++)
            {
                if(a[i].charAt(j)>c2[j])
                {
                    c2=a[i].toCharArray();
                    break;
                }
                else
                    if(a[i].charAt(j)==c2[j])
                        continue;
                    else
                        if(a[i].charAt(j)<c2[j])
                            break;
                        
            }
  
        }
        
        for(char t:c1)
            smallest+=t;
        for(char t:c2)
            largest+=t;
        
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
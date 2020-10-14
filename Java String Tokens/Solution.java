import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        ArrayList<String> a=new ArrayList<String>();
        String t="";
        // Write your code here.
    for(int i=0; i<s.length(); i++)
    {
if((s.charAt(i)>='a' && s.charAt(i)<='z')||(s.charAt(i)>='A' && s.charAt(i)<='Z'))
    t+=s.charAt(i);
    else
        {
        if(t!="")
        a.add(t);
        t="";
        }

    }
    if(t!="" && (s.charAt(s.length()-1)>='a' && s.charAt(s.length()-1)<='z')||(s.charAt(s.length()-1)>='A' && s.charAt(s.length()-1)<='Z'))
        a.add(t);
    System.out.println(a.size());
    for(String z: a)
    System.out.println(z);


        scan.close();
    }
}




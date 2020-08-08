import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        a=a.toLowerCase();
        b=b.toLowerCase();
        char[] ch = new char[a.length()];
        int[] f=new int[a.length()];
        int[] f1=new int[a.length()];
        if(a.length()==b.length())
        {
for(int i=0;i<a.length(); i++)
    ch[i]=a.charAt(i);
for(int i=0; i<ch.length;i++)
{
    int sum=0;
for(int j=0; j<ch.length;j++)
{
if(a.charAt(j)==ch[i])
sum+=1;
}
f[i]=sum;
}
for(int i=0; i<ch.length;i++)
{
    int sum=0;
for(int j=0; j<ch.length;j++)
{
if(b.charAt(j)==ch[i])
sum+=1;
}
f1[i]=sum;
}
int ctr=0;
for(int k=0; k<ch.length; k++)
{
    if(f[k]==f1[k])
    ctr++;
    else
    break;
}
if(ctr==ch.length)
return(true);
else
return(false);
        }
        else
        return(false);
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
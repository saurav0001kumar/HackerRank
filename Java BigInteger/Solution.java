/*
Java BitInteger class contains add() and multiply().
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    BigInteger a=sc.nextBigInteger();
    BigInteger b=sc.nextBigInteger();
    System.out.println(a.add(b)+"\n"+a.multiply(b));
    sc.close();
    }
}
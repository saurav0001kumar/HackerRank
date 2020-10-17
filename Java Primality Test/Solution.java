/*
Java Primality Test of very large number using isProbablePrime() inside BitInteger class.
*/
import java.math.BigInteger;
import java.util.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
       BigInteger n = scanner.nextBigInteger();
        if(n.isProbablePrime(1))
        System.out.println("prime");
        else
        System.out.println("not prime");
        scanner.close();
    }
}

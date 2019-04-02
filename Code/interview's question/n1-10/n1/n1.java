/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;



/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static final int MAX_UNIT = 99;
		
	public static boolean containsPairWithSum(int[] a, int x) {
	    Arrays.sort(a);
	    for (int i = 0, j = a.length - 1; i < j;) {
	        int sum = a[i] + a[j];
	        if (sum < x)
	            i++;
	        else if (sum > x)
	            j--;
	        else
	            return true;
	    }
	    return false;
	}
	
	public static void main(String[] args){
		System.out.println("Enter a size for an array: ");
		Scanner scanner = new Scanner(System.in);
		int size = scanner.nextInt();
	
		int a[] = new int[size];
		for(int i = 0; i < size; i ++)
		{
			a[i] = (int)(Math.random()*MAX_UNIT);
		}
	
		System.out.println("Enter a number: ");	
	
		int sum = scanner.nextInt();
		
		System.out.println("Can you get the sum "+sum+" with the values of "+Arrays.toString(a)+" ?");
	
		System.out.println(containsPairWithSum(a, sum));
	}
}
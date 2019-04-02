This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?


```java
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
```
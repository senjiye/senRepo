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
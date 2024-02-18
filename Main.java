public class Main {

    public static int findMax(int[] intArray) {
        int maxNum = intArray[0];

        for (int j : intArray) {
            if (j > maxNum)
                maxNum = j;
        }

        return maxNum;
    }

    public static void main(String[] args) {
        int[] intArray = {30, 5, 0, 44, 15, 225, 9};

        int maxNum = findMax(intArray);

        System.out.println("Maximum number = " + maxNum);
    }
}

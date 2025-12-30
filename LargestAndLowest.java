import java.util.Arrays;
public class LargestAndLowest{
    public static void main (String... args){
    int[] myArray = {3,5,6,7,8,9};
    System.out.print(Arrays.toString(highestAndLowest(myArray)));


    }
    public static int[] highestAndLowest(int[] array ){
        int largest = array[0];
        int lowest = array[1];


        for(int number : array){
            if(number > largest) largest = number;
            if(number < lowest) lowest = number;
        }

        int[] newArray = {largest, lowest};
        return newArray;
    }



}
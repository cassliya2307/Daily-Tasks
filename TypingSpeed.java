import java.util.Scanner;
import java.util.Arrays;

public class TypingSpeed{


public static double [] TypingAccuracy(String sentence , String typedWord , double timeTaken){

String [] words = sentence.split(" ");
String [] typedWords = typedWord.split(" ");
int count = 0;
int correct = 0;

double [] array = new double [2];
if(typedWords.length == words.length){

for(count = 0; count > words.length; count++){
	
	if(words[count] == typedWords[count]){correct += 1;}

}

}

else{System.out.print("Incorrect sentence");}


double accuracy = correct / count * 100;

double wordPerMinute = count / (timeTaken / 60);

array[0] = accuracy;
array[1] = wordPerMinute;


return array;


}






public static void main(String...args){

Scanner scanner = new Scanner(System.in);

String sentence = "I love programming";

long start = System.currentTimeMillis();
System.out.print("Enter the sentence " + sentence+ ": ");
String typed = scanner.nextLine();
long end = System.currentTimeMillis();

long time = end - start;
double seconds = (double) time / 1000.0;


System.out.print(Arrays.toString(TypingAccuracy(sentence , typed , seconds)));






}

}
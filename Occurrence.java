public class Occurrence{
public static int Occurrence(String characters){
String letter = characters.toLowerCase();
int occurrence = 0;
	for(int index = 0; index < letter.length(); index++){
	int count = 0;
	for(int counter = index + 1; counter < letter.length(); counter++){
	if(letter.charAt(index) == letter.charAt(counter)){ count++;}
		}
		
	if (count >= 1) {occurrence++;}
	}
	return occurrence;

}

}
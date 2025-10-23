import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class LowercaseToUppercaseTest{

	@Test
	public void testThatItConvertsItToUppercase(){
	// ARRANGE

	ToUpperCase toUpperCase = new ToUpperCase();

	//ACT
	String userInput = toUpperCase.upperString("A");

	//ASSERT
	assertEquals(userInput, "A");


	}

	












}

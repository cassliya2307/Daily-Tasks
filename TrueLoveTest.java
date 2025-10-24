import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class TrueLoveTest{


	@Test
	public void testThatItReturnsTrueWhenTheFirstInputIsOddAndTheSecondInputEven(){
	// ARRANGE

	Truelove truelove = new Truelove();

	//ACT
	int flower_petals_1 = truelove.loveSparks(True);
	int flower_petals_2 = truelove.loveSparks(True);

	//ASSERT
	assertEquals(flower_petals_1 , flower_petals_2, True);


	}





















}

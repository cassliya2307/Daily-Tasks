import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class LibraryTest{
	@Test
	public void testThatLibraryHasNoBook(){
	// ARRANGE

	Library library = new Library();

	//ACT
	int result = library.totalNumberOfBooks();

	//ASSERT
	assertEquals(result,0);


	}

	@Test
	public void testThatOneBookIsAddedToTheLibraryAndTheTotalNumberOfBooksIsOne(){
	// ARRANGE

	Library library = new Library();
	
	//ACT
	String response = library.addBook("Things Fall Apart");

	//ASSERT
	assertEquals(response, "Book Added Successfully");


	}










}
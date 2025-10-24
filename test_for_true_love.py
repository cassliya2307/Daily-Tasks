import unittest

from True_love import*
class TestForLoveAccurayWithPetals(unittest.TestCase):

	def test_if_they_input_odd_and_even_it_will_return_true(self):
		actual = true_love(4,3)
			
		expected = True
		
		self.assertEqual(actual , expected)

		

	def test_if_they_input_even_and_odd_it_will_return_true(self):
		actual = true_love(5,6)
			
		expected = True
		
		self.assertEqual(actual , expected)


	def test_if_they_input_even_and_even_it_will_return_false(self):
		actual = true_love(10 , 8)
			
		expected = False
		
		self.assertEqual(actual , expected)

	def test_if_they_input_odd_and_odd_it_will_return_true(self):
		actual = true_love(5, 15)
			
		expected = False
		
		self.assertEqual(actual , expected)



	def test_if_they_enter_a_wrong_input(self):
		wrong_input_1 = "anime"

		wrong_input_2 = 12.67


		self.assertRaises(TypeError,wrong_input_1 , wrong_input_2)



import unittest

import lowercase_to_uppercase_function

class TestForConversionOfLowerCaseToUpperCase(unittest.TestCase):


	def test_for_wrong_input_by_the_user_in_lower_to_upper(self):
		wrong_input_1 = 12
		self.assertRaises(TypeError, wrong_input_1)

	
	
	def test_for_wrong_input(self):
		wrong_input_2 = 12.9
		self.assertRaises(TypeError, wrong_input_2)


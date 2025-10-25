import unittest

from convert_string_to_array import*


class TestToConvertStringToList(unittest.TestCase):

	def test_if_the_function_returns_a_list(self):
		actual = convert_string_to_array("my name is")
		expected = ["my" , "name" , "is"]
		self.assertEqual(actual , expected);
		

	def test_if_user_inputs_wrong_type(self):
		wrong_input_1 = 123
		wrong_input_2 = 32.28
		self.assertRaises(TypeError, wrong_input_1, wrong_input_2)
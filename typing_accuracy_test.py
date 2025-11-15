import unittest

from typing_accuracy import*


class TestTheTypingAccuracyConsoleApp(unittest.TestCase):
	
	def test_the_typing_accuracy_function(type):
		actual = get_typing_accuracy("Anime is amazing isn't it?", "Anime is amazing isn't it?")
		expected = (10.01 , 0.00, 100.00)
		type.assertEqual(actual , expected)
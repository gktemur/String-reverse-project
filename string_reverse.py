def reverse_string(input_string):
  """"
  Reverses the given string.

  Args:
      input_string (str): The string to reverse.
  Returns: 
      str: The reversed string.
  """
  return input_string[::-1]

def main():
  """
  Main function to execute the string to reversal program.
  """
  user_input = input ("Enter a string to reverse: ")
  reversed_string = reverse_string(user_input)
  print(f"Reversed string: {reversed_string}")

if __name__== "__main__":
  main()

import unittest

class TestStringMethods(unittest.TestCase):
  """
  Unit test class for testing reverse_string function.
  """
  def test_reverse_string(self):
    self.assertEqual(reverse_string("hello"), "olleh")
    self.assertEqual(reverse_string("Python"), "nohtyP")
    self.assertEqual(reverse_string(""), "")
    self.assertEqual(reverse_string("a"), "a")

if __name__ =='__main__':
  unittest.main()
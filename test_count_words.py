"""This is the testing area for the count_words.py
The tests ensures that we cover every available user option/usage
to make sure that we have the error handled before the
user knows about it
- We use pytest module to test our code
- pip install pytest if you don't have it
- usually (perhaps not always -- check this)
- the word test appears at the beginning of the method.
check if by having test anywhere in your testing script
filename has pytest recognize the file as a test.
"""
import pytest
# pylint: disable=C0303
# pylint: disable=R0201
from count_words import WordCounter
INST = WordCounter()
class TestWordCounter:
    """This is the class where tests are implemented
    """
    def test_empty(self):
        """Testing for an empty string
        """
        text = ""
        assert INST .count_words(text) == 0
    
    def test_one(self):
        """Testing for one word
        """
        text = "Cascabel"
        assert INST .count_words(text) == 1
    
    def test_multiple_words(self):
        """Testing for multiple words
        """
        text = "I study data science"
        assert INST .count_words(text) == 4
    
    def test_hyphens(self):
        """Testing for hyphens
        """
        text = "How-are-you-doing?"
        assert INST .count_words(text) == 4
    
    def test_linebreaks(self):
        """Testing for linebreaks
        """
        text = "\nHow\nare\nyou\ndoing"
        assert INST .count_words(text) == 4
    
    def test_hmtl(self):
        """Testing for html
        """
        text = "<h1> I am a student </h1>"
        assert INST .count_words(text) == 4
        
    def test_spaces(self):
        """Testing for white spaces
        """
        text = "  test spaces   "
        assert INST .count_words(text) == 2
    
    def test_data_type_error(self):
        """Testing for wrong data type
        """
        text = ["name"]
        with pytest.raises(Exception) as my_error:
            INST .count_words(text)
        assert "Strings only" in str(my_error.value)

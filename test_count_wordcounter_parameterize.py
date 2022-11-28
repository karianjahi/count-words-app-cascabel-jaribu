"""
Here we want to parameterize the tests - Running all tests at once
We write all the tests as one in a list of lists
"""
import pytest
from count_words import WordCounter
INST = WordCounter()
# pylint: disable=C0303
# pylint: disable=W0622
MY_TESTS = [
    ("Cascabel", 1),
    ("", 0),
    ("How-are-you-doing?", 4),
    ("I study data science", 4),
    ("\nHow\nare\nyou\ndoing", 4),
    ("<h1> I am a student </h1>", 4),
    ("  test spaces   ", 2) 
]

@pytest.mark.parametrize('input, output', MY_TESTS)
def test_all(input, output):
    """This function performs automated testsing at once

    Parameters
    ----------
    input : str
        sentence/word
    output : int
        no. of words in a string or sentence
    
    Returns
    -------
        None
    """
    assert INST.count_words(input) == output
    
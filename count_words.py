"""
This code counts words in a string
"""
import re
from bs4 import BeautifulSoup
class WordCounter:
    """
    This is the class that houses the attributes and methods
    for our counting application
    """
    def __init__(self):
        """
        This is the class constructor.
        Defines all our global attributes and methods.
        This is usually the first port of entry to our code
        """
        ...
    
    def count_words(self, text):
        """This is the method that counts the words

        Parameters
        ----------
        text : str
            A word or a sentence

        Returns
        -------
        int
            number of words in the corpus/sentence
        """
        assert isinstance(text, str), "Strings only"
        text = self._run_text_through_html_filter(text)
        text = self._remove_hyphens(text)
        splits =  text.split()
        count = len(splits)
        return count
    
    def _remove_hyphens(self, text):
        """Remove hyphes if they exist
        
        Parameters
        ----------
        text : str
            A word or a sentence

        Returns
        -------
        str
            text without hyphens
        """
        return re.sub("-", " ", text)
    
    def _run_text_through_html_filter(self, text):
        """Extract text from a possible html string

        Parameters
        ----------
        text : str
            string that might contain html

        Returns
        -------
        _type_
            str
        """
        soup = BeautifulSoup(text, "html.parser")
        return soup.text
        

if __name__ == "__main__":
    inst = WordCounter()
    # sentence = ["I am a student"]
    # sentence = "I-am-a-student"
    sentence = "<h1> Testing html </h>"
    # print(inst._run_text_through_html_filter(sentence))
    
    print(inst.count_words(sentence))
        
        

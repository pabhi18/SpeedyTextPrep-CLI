import re
from gensim.parsing.preprocessing import remove_stopwords

#TextCleaning
class TextCleaning:
    def __init__(self, data):
        if not isinstance(data, str):
            raise ValueError("Input data must be a string.")
        self.data = data

    #LowerCasing Function
    def lowercasing(self):
        try:
            clean_text = self.data.lower()
        except AttributeError:
            raise ValueError("Input data must be a string.")
        return clean_text

    #Removing Punctuation Function
    def removing_punctuation(self):
        try:
            clean_text = re.sub(r'[^\w\s]', '', self.data)
        except TypeError:
            raise ValueError("Input data must be a string.")
        return clean_text
    
    #Removing Numbers
    def removing_numbers(self):
        try:
            clean_text = re.sub(r'\d', '', self.data)
        except TypeError:
            raise ValueError("Input data must be a string.")
        return clean_text

    #Removing Stopwords
    def removing_stopwords(self):
        try:
            clean_text = remove_stopwords(self.data)
        except AttributeError:
            raise ValueError("Input data must be a string.")
        return clean_text

    #Removing Special Character
    def removing_special_chars(self):
        try:
            clean_text = re.sub(r'[^a-zA-Z0–9\s]', '', self.data)
        except TypeError:
            raise ValueError("Input data must be a string.")
        return clean_text
    
    #Removing HTML Tags
    def removing_html_tags(self):
        try:
            re_html = re.compile(r'<.*?>')
            clean_text = re_html.sub('', self.data)
        except TypeError:
            raise ValueError("Input data must be a string.")
        return clean_text


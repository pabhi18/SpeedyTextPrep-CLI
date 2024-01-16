import nltk
from gensim.parsing.preprocessing import remove_stopwords
import re

#TextCleaning
class TextCleaning:
    def __init__(self, data):
        self.data = data

    #LowerCasing Function
    def lowercasing(self):
        clean_text = self.data.str.lower()
        return clean_text
    
    #Removing Punctuation Function
    def removing_punctuation(self):
        clean_text = re.sub(r'[^\w\s]', '', self.data)
        return clean_text
    
    #Removing Numbers
    def removing_numbers(self):
        clean_text = re.sub(r'\d', '', self.data)
        return clean_text

    #Removing Stopwords
    def removing_stopwords(self):
        clean_text = remove_stopwords(self.data)
        return clean_text
    
    #Removing Special Character
    def exclude_special_chars(self):
        clean_text = re.sub(r'[^a-zA-Z0–9]', '', self.data)
        return clean_text
    
    #Removing HTML Tags
    def removal_html_tags(self):
        re_html = re.compile(r'<.*?>')
        clean_text = re_html.sub('', self.data)
        return clean_text
    

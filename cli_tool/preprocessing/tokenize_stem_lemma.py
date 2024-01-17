import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

class Tokenize:
    @staticmethod
    def __init__(self, data):
        if not isinstance(data, str):
            raise ValueError("Input data must be a string.")
        self.data = data

    def tokenization(self):
        try:
            tokenized_text = word_tokenize(self.data)
        except TypeError:
            raise ValueError("Input data must be a string.")
        return tokenized_text
    
    def stemming(self):
        try:
            stemmed_text = [ps.stem(w) for w in self.tokenization()]
        except TypeError:
            raise ValueError("Input data must be a string.")
        return stemmed_text
    
    def lemmatization(self):
        try:
            lemmatized_text = [lemmatizer.lemmatize(w) for w in self.tokenization()]
        except TypeError:
            raise ValueError("Input data must be a string.")
        return lemmatized_text

        

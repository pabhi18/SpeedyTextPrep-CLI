import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

class Tokenize:
    def __init__(self, data):
        self.data = data

    def tokenization(self):
        tokenized_text = word_tokenize(self.data)
        return tokenized_text
    
    def stemming(self):
        stemmed_text = [ps.stem(w) for w in self.tokenization()]
        return stemmed_text
    
    def lemmatization(self):
        lemmatized_text = [lemmatizer.lemmatize(w) for w in self.tokenization()]
        return lemmatized_text

        

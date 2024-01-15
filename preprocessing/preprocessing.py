import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

class preprocessing:
    def __init__(self, data):
        self.data = data

    def tokenizations(self):
        tokenized_text = word_tokenize(self.data)
        return tokenized_text
    
    def stemming(self):
        stemmed_text = [(self.data.stem(w)) for w in self.data]
        return stemmed_text
    
    def lemmatization(self):
        lemmatized_text = [(lemmatizer.lemmatize(w)) for w in self.data]
        return lemmatized_text
    

        

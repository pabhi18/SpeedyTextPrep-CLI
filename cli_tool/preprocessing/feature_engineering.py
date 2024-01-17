from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import pandas as pd

tfidf_vectorizer = TfidfVectorizer()

class FeatureEngineering:
    @staticmethod
    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Input data must be a list of strings.")
        self.data = data

    def tf_idf(self):
        try:
            tfidf_matrix = tfidf_vectorizer.fit_transform(self.data)
            feature_names = tfidf_vectorizer.get_feature_names_out()
            df_tfidf = pd.DataFrame(data=tfidf_matrix.toarray(), columns=feature_names)
            return df_tfidf
        except Exception as e:
            raise RuntimeError(f"Error in TF-IDF feature engineering: {str(e)}")

    def embedding(self):
        try:
            model = Word2Vec(sentences=self.data, vector_size=100, window=5, min_count=1, workers=4, sg=0)
            embedding = [model.wv[word] for sentence in self.data for word in sentence if word in model.wv]
            return embedding
        except Exception as e:
            raise RuntimeError(f"Error in word embedding: {str(e)}")


from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
tfidf_vectorizer = TfidfVectorizer()
import pandas as pd

class FeatureEngineering:
    def __init__(self, data):
        self.data = data

    def tf_idf(self):
        tfidf_matrix = tfidf_vectorizer.fit_transform(self.data)
        feature_names = tfidf_vectorizer.get_feature_names_out()
        df_tfidf = pd.DataFrame(data=tfidf_matrix.toarray(), columns=feature_names)

        return df_tfidf

    def embedding(self):
        model = Word2Vec(sentences=self.data, vector_size=100, window=5, min_count=1, workers=4, sg=0)
        embedding = [model.wv[word] for sentence in self.data for word in sentence if word in model.wv]
        return embedding


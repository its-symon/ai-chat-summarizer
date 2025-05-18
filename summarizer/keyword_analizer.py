from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords(user_msgs, ai_msgs, num_keywords=5):
    all_docs = user_msgs + ai_msgs
    
    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer(
        max_df=0.85,               # Ignore terms that appear in >85% of documents
        min_df=2,                  # Ignore terms that appear in fewer than 2 documents
        stop_words='english',      # Remove English stopwords
        use_idf=True,              # Enable IDF weighting
        ngram_range=(1, 1),        # Only consider single words (can be changed to include phrases)
        sublinear_tf=True          # Apply sublinear tf scaling (1 + log(tf))
    )
    
    # Fit and transform the documents
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_docs)
    
    # Get feature names (words)
    feature_names = np.array(tfidf_vectorizer.get_feature_names_out())
    
    # Calculate the average TF-IDF score for each word across all documents
    tfidf_mean = np.array(tfidf_matrix.mean(axis=0)).flatten()
    
    # Get the indices of top N keywords based on average TF-IDF score
    top_indices = tfidf_mean.argsort()[-num_keywords:][::-1]
    
    # Get the top keywords and their scores
    top_keywords = [(feature_names[i], tfidf_mean[i]) for i in top_indices]
    
    return top_keywords

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def preprocess_text(line: str):
    line = word_tokenize(line)
    line = [word.lower() for word in line if word.isalpha() and word.lower() not in stop_words]
    return ' '.join(line)
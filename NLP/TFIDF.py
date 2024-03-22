import nltk

paragraph = """In 3000 years of our history, people from all over the world have been drawn to India's rich tapestry. This legacy of exchange inspires my three visions for India's future. Firstly, I see India as a global leader in innovation, drawing on its scientific heritage and youthful population to tackle pressing challenges  like climate change and sustainable development. Secondly, I envision India as a vibrant hub of cultures, where ancient traditions live alongside contemporary expressions, creating a unique and dynamic society. Finally, I dream of India as a beacon of peace and collaboration, fostering understanding and cooperation between nations, much like the famous scholars and traders who traversed the Silk Road centuries ago. These are just some of the ways India can continue to inspire the world in the next 3,000 years.""" 

#Cleaning the texts
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
print(corpus)

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
print(X)
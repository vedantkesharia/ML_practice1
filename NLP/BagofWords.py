import nltk

paragraph = """In 3000 years of our history, people from all over the world have been drawn to India's rich tapestry. This legacy of exchange inspires my three visions for India's future. Firstly, I see India as a global leader in innovation, drawing on its scientific heritage and youthful population to tackle pressing challenges  like climate change and sustainable development. Secondly, I envision India as a vibrant hub of cultures, where ancient traditions live alongside contemporary expressions, creating a unique and dynamic society. Finally, I dream of India as a beacon of peace and collaboration, fostering understanding and cooperation between nations, much like the famous scholars and traders who traversed the Silk Road centuries ago. These are just some of the ways India can continue to inspire the world in the next 3,000 years.""" 

#Cleaning the texts

import re  #regular expression
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)
corpus = [] #after cleaning we will store it in this list
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

print(corpus)

#Creating Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
print(X)


#X = cv.fit_transform(corpus).toarray(): This line performs the feature extraction process. It takes the corpus (a collection of text documents) and transforms it into a matrix of token counts. fit_transform() is a method of the CountVectorizer class, which learns the vocabulary dictionary and returns a document-term matrix. .toarray() converts the sparse matrix representation into a dense NumPy array. The resulting matrix X contains the token counts, where each row represents a document in the corpus and each column represents a unique token (word) in the entire corpus.
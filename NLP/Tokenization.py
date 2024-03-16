import nltk

nltk.download()

paragraph = """In 3000 years of our history, people from all over the world have been drawn to India's rich tapestry. This legacy of exchange inspires my three visions for India's future. Firstly, I see India as a global leader in innovation, drawing on its scientific heritage and youthful population to tackle pressing challenges  like climate change and sustainable development. Secondly, I envision India as a vibrant hub of cultures, where ancient traditions live alongside contemporary expressions, creating a unique and dynamic society. Finally, I dream of India as a beacon of peace and collaboration, fostering understanding and cooperation between nations, much like the famous scholars and traders who traversed the Silk Road centuries ago. These are just some of the ways India can continue to inspire the world in the next 3,000 years.""" 

sentences = nltk.sent_tokenize(paragraph)

words = nltk.word_tokenize(paragraph)

print("Sentences are: ")
print(sentences)

print("Words are: ")
print(words)
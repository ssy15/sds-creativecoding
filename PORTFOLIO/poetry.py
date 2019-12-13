!pip install markovify
import markovify

wordlist = text.split(" ")
random.randint(1,6)
!pip install textBlob
from textblob import TextBlob

import nltk
nltk.download('averaged_perceptron_tagger')

import nltk
nltk.download('punkt')

adjectives=[]
for word,tag in blob.tags:
  if tag == "JJ":
   adjectives.append(word)

nouns=[]
for word,tag in blob.tags:
  if tag == "NN":
    nouns.append(word)

with open("poemnovel.txt") as f:
    text = f.read()
text_model = markovify.Text(text)

for i in range(5):
  a = random.choice(adjectives)
  n = random.choice(nouns)
  print(text_model.make_short_sentence(50))
  print(a,n)

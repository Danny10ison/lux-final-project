import numpy as np
import nltk
import string
import random

f = open('chatbox.txt', 'r', errors='ignore')
raw_doc = f.read()
raw_doc_lower = raw_doc.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_token = nltk.sent_tokenize(raw_doc_lower)
word_token = nltk.word_tokenize(raw_doc_lower)

#sent_token[:2]
#word_token[:2]

lemmer = nltk.stem.WordNetLemmatizer()

def LemToken(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemToken(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREET_INPUTS = ("hello", "hi", "greetings", "sup", "whats up", "hey")
GREET_RESPONSE = ["hi", "hey", "nods", "hi there", "hello", "I am glad! You are talking to me"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSE)

# Response generation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo1_response=''
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidVec.fit_transform(sent_token)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf==0):
        robo1_response=robo1_response+"Sorry, I dont understand"
        return robo1_response
    else:
        robo1_response = robo1_response+sent_token[idx]
        return robo1_response

flag = True
print("Bot: My name is Mann. Say Hi, or bye to end the conversation")
while(flag):
    user_response = input()
    user_response = user_response.lower()
    if(user_response != 'bye'):
        if (user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("Bot: Welcome")
        else:
            if(greet(user_response) != None):
                print("Bot: "+greet(user_response))
            else:
                sent_token.append(user_response)
                word_token = word_token+nltk.word_tokenize(user_response)
                final_words = list(set(word_token))
                print("Bot: ", end="")
                print(response(user_response))
                sent_token.remove(user_response)
    else:
        flag=False
        print("Bot: Goodbye! Take care ^()^")




















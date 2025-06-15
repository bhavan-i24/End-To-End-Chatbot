import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

corpus = []
tags = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    sim = cosine_similarity(user_vec, X)
    idx = sim.argmax()
    tag = tags[idx]
    return random.choice(responses[tag])

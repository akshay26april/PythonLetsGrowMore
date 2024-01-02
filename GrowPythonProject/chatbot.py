import nltk
import numpy as np
import random
import string
import pickle
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Sample chatbot data
corpus = [
    'What is your name?',
    'How are you?',
    'What is the time?',
    'Tell me a joke.',
    'Who created you?',
    'What is the meaning of life?',
    'Exit'
]

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Preprocess data
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(tokens)

corpus = [preprocess_text(sentence) for sentence in corpus]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Save vectorizer and X for later use
with open('vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

with open('X.pkl', 'wb') as X_file:
    pickle.dump(X, X_file)

# Training and testing datasets
training_data = [
    "What is your name?",
    "How are you?",
    "What is the time?",
    "Who created you?"
]

testing_data = [
    "Tell me a joke.",
    "What is the meaning of life?",
    "Exit"
]

# Create response dictionary
responses = {
    "What is your name?": "I am a chatbot.",
    "How are you?": "I am doing well, thank you!",
    "What is the time?": "I don't have a watch.",
    "Who created you?": "I was created by a developer.",
    "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
    "What is the meaning of life?": "The meaning of life is subjective and varies for each individual.",
    "Exit": "Goodbye! Have a great day."
}

# Train the chatbot
def train_chatbot(training_data, responses):
    lemmatized_training_data = [preprocess_text(sentence) for sentence in training_data]
    y = np.array([responses[data] for data in training_data])

    # Create and train a simple classifier (e.g., Linear SVM)
    from sklearn.svm import SVC
    classifier = SVC(kernel='linear')
    classifier.fit(X, y)

    # Save the trained classifier
    with open('classifier.pkl', 'wb') as classifier_file:
        pickle.dump(classifier, classifier_file)

# Train the chatbot
train_chatbot(training_data, responses)

# Test the chatbot
def test_chatbot(testing_data):
    with open('classifier.pkl', 'rb') as classifier_file:
        classifier = pickle.load(classifier_file)

    for test_sentence in testing_data:
        test_sentence = preprocess_text(test_sentence)
        test_vector = vectorizer.transform([test_sentence])
        prediction = classifier.predict(test_vector)
        print(f"User: {test_sentence}")
        print(f"Chatbot: {prediction[0]}\n")

# Test the chatbot
test_chatbot(testing_data)

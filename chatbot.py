import random
import nltk
import spacy
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("wordnet")

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! How can I help?"],
    "goodbye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "default": ["I'm sorry, I didn't understand that.", "Can you rephrase?", "I'm not sure how to respond to that."],
}

# Function to check for synonyms (basic NLP)
def check_synonyms(word, category):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return any(synonym in category for synonym in synonyms)

# Function to process user input
def process_input(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    doc = nlp(user_input)

    # Rule-based intent detection
    if any(token in user_input for token in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    elif any(token in user_input for token in ["bye", "goodbye", "see you"]):
        return random.choice(responses["goodbye"])
    elif any(token in user_input for token in ["thanks", "thank you"]):
        return random.choice(responses["thanks"])
    
    # Check for entities using spaCy
    if doc.ents:
        for entity in doc.ents:
            if entity.label_ == "PERSON":
                return f"It's nice to talk to you, {entity.text}!"
            elif entity.label_ == "GPE":
                return f"Tell me more about {entity.text}! I love learning about places."
    
    # Synonym-based handling
    if any(check_synonyms(token, ["help", "assist", "support"]) for token in tokens):
        return "How can I assist you? Feel free to ask anything."

    # Default response
    return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = process_input(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

# Define the knowledge base
kb = {
    "admission requirements": "The admission requirements include a high school diploma",
    "academic programs": "The university offers a wide range of academic programs, including business, engineering, arts, and sciences.",
    "student services": "The university provides various student services, including academic advising, career counseling, and mental health support."
    }

# Define a function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    preprocessed_text = ' '.join(lemmatized_tokens)
    return preprocessed_text

# Define a function to answer a user's question
def answer_question(question):
    preprocessed_question = preprocess_text(question)
    for kb_question, answer in kb.items():
        if preprocessed_question in preprocess_text(kb_question):
            return answer
    return "Kindly call us on 0773811271 for further questions"

# Define the interactive interface
def interact_with_user():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("Please enter your question: ")
        answer = answer_question(user_input)
        print("Answer:", answer)

# Call the interact_with_user function
interact_with_user()
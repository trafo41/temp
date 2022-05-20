import re
keywords = {'greet': ["hello","hi","hey"] , 
            'goodbye': ["bye","farewell"] ,
            'thankyou': ["thank","thnx"]}

patterns = {}
responses = {'greet': 'hello you!', 'goodbye' : 'good bye for now' , 'thankyou': 'you are very welcome'}

for intent, keys in keywords.items():
    # Create regular expressions and compile them into pattern objects
    patterns[intent] = re.compile('|'.join(keys))

print(patterns)


# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        if re.search(pattern, message):                                        # Check if the pattern occurs in the message 
            matched_intent = intent
    print(matched_intent)
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

def send_message(message):
    return respond(message)

# Send messages
print(send_message("hello!"))
print(send_message("bye byeee"))
print(send_message("thanks very much!"))
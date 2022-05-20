import re
def find_name(message):
    name = None
    name_keyword = re.compile('name|call')                                 # Create a pattern for checking if the keywords occur    

    name_pattern = re.compile('[A-Z]{1}[a-z]*')                            # Create a pattern for finding capitalized words
    if name_keyword.search(message):        
        name_words = name_pattern.findall(message)                         # Get the matching words in the string
        if len(name_words) > 0:
            name = ' '.join(name_words)                                    # Return the name if the keywords are present
    return name


def respond(message):
    # Find the name
    name = find_name(message)
    if name is None:
        return "Hi there!"
    else:
        return "Hello, {0}!".format(name)

# Send messages
print(respond("my name is David Copperfield"))
print(respond("call me Ishmael"))
print(respond("People call me Cassandra"))
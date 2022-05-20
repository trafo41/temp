import spacy
nlp = spacy.load('en')
print(nlp.vocab.vector_length)

doc = nlp('hello can you help me?')
for token in doc:
    print('{} : {}'.format(token,token.vector[:3]))
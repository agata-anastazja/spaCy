# Import the English language class
from spacy.lang.en import English

# Create the nlp object
nlp = English()

# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")

# Iterate over tokens in a Doc
# for token in doc:
#     print(token.text)

# Index into the Doc to get a single Token
# token = doc[1]

# # Get the token text via the .text attribute
# print(token.text)

# A slice from the Doc is a Span object
span = doc[1:4]

# Get the span text via the .text attribute
print(span.text)

doc = nlp("It costs $5.")
print('Index:   ', [token.i for token in doc])
print('Text:    ', [token.text for token in doc])

print('is_alpha:', [token.is_alpha for token in doc])
print('is_punct:', [token.is_punct for token in doc])
print('like_num:', [token.like_num for token in doc])
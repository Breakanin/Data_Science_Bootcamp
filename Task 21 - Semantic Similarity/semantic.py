# I'm performing the code using 'en_core_web_sm' english language package

import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# my own examples with 'en_core_web_sm' language package

nlp = spacy.load('en_core_web_sm')
word1 = nlp("tree")
word2 = nlp("house")
word3 = nlp("helicopter")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('tree apple house helicopter')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# I'm performing the same code using different english language package

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# my own examples with 'en_core_web_md' language package

nlp = spacy.load('en_core_web_md')
word1 = nlp("tree")
word2 = nlp("house")
word3 = nlp("helicopter")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('tree apple house helicopter')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


'''
The model thinks that "Where did my dog go" is more similar to "I will name my dog Diana"
than to "I'd like my boat back", which makes sense because both sentences have the word "dog" in them.
However, the model gives a higher score for this pair when using the "en_core_web_md", which suggests
that the medium package can better capture the meaning of the sentences than the small package.
'''

'''

'''
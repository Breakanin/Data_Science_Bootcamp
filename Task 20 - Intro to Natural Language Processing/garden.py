
import spacy

nlp = spacy.load('en_core_web_sm')

# store gardenpathSentences in a list
gardenpathSentences = ["The complex houses married and single soldiers and their families.", 
"The florist sent the bouquet of flowers was very flattered.",
"Mary gave the child a Band-Aid.",
"That Jill is never here hurts.",
"The cotton clothing is made of grows in Mississippi."]


# tokenise each sentence in the list and perform named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print("Here are tokens from the sentence: ")
    print([(token, token.orth_, token.orth) for token in doc])
    print("The entities are: ")
    print([(entity, entity.label_, entity.label) for entity in doc.ents])


# look up and print the meaning of entities
print("There are our entities explained: 'PERSON' and 'GPE' ")
print(spacy.explain("PERSON"))
print(spacy.explain("GPE"))

# I looked up the following entities:

# PERSON: People, including fictional
# PERSON refers to people’s names or nicknames.

# GPE: Countries, cities, states
# GPE refers to geo-political entities, such as countries, cities, states or regions.

# Did the entity make sense in terms of the word associated with it?
# They make sense in terms of the words associated with them, such as Jill, which is a person and Mississippi, is a State in USA.
import spacy

#  Loading the model
nlp = spacy.load('en_core_web_md')

# Creating model objects
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Printing similarities between the words
print("\n---------- Similarity With SpaCy ----------\n")
print(word1, word2, word1.similarity(word2))
print(word3, word2, word3.similarity(word2))
print(word3, word1, word3.similarity(word1))

"""
Interestingly, cat and monkey share a lot more similarities (59%) 
being animals, than they each share with banana, a fruit.

The similarity between monkey and banana (40%) is also noteworthy, given
that monkeys love to eat bananas and the model is able to find
something the two have in common.

Even though cat and monkey are quite similar (60%), and monkey and banana
also share a good amount of similarity (40%), cats do not like bananas and
this is evident in the dissimilarity between the two (22% similarity score).
"""
print("\n---------- Another example ----------\n")
nlp2 = spacy.load('en_core_web_md')

word4 = nlp2("phone")
word5 = nlp2("laptop")
word6 = nlp2("drink")

#Printing similarities
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

print("\n---------- Working with vectors ----------\n")
tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print("\n---------- Working with sentences ----------\n")
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go", "Hello, there is my car", "I\'ve lost my cat in my car", "I\'d like my boat back", "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence, "-", similarity)
print("A carregar corpus...")
from nltk.corpus import wordnet as wn

word = 'dog'

print("Imprimir lista de sinonimos:")
print(wn.synsets(word))

print("\nImprimir sinónimo a sinónimo:")
for synset in wn.synsets(word):
    print()
    print(synset)
    for lemma in synset.lemmas():
        print(lemma.name())

print("\nDefinições da palavra " + word + ":")

for synset in wn.synsets(word):
    print(synset.definition())

dog = wn.synsets(word)[0]

print("\nImprimir hipónimos e hiperónimos:")
print(dog.hypernyms()[:3])
print(dog.hyponyms()[:10])

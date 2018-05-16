print("A carregar corpus...")
from nltk.corpus import wordnet as wn

word = 'intelligence'

print("Lista de sinonimos:")
print(wn.synsets(word))

print("\nSinónimos:")
for synset in wn.synsets(word):
    print()
    print(synset)
    for lemma in synset.lemmas():
        print(lemma.name())

print("\nDefinições da palavra " + word + ":")

for synset in wn.synsets(word):
    print(synset.definition())

intelligence = wn.synsets(word)[0]

print("\nHipónimos e Hiperónimos:")
print(intelligence.hypernyms()[:3])
print(intelligence.hyponyms()[:10])

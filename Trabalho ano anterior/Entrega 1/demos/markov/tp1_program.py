"""Gera um modelo de markov com a ordem dada pelo utilizador"""

import re
from collections import defaultdict, deque, Counter

order = int(input("Model order:"))
textSize = 100


def tokenize(file_path, tokenizer):
    with open(file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            for token in tokenizer(line.lower().strip()):
                yield token


def words(file_path):
    return tokenize(file_path, lambda s: re.findall(r"[\w']+|[.!?]", s))


def fcm(stream, model_order):
    if model_order == 0:
        model = []
        stats = Counter()

        for token in stream:
            model.append(token)
            stats[token] += 1
        return model, stats
    else:
        model, stats = defaultdict(Counter), Counter()
        circular_buffer = deque(maxlen=model_order)

        if model_order == 0:
            print('Model order = 0')
            circular_buffer = deque(maxlen=model_order + 1)

        for token in stream:
            prefix = tuple(circular_buffer)
            circular_buffer.append(token)
            if len(prefix) == model_order:
                stats[prefix] += 1
                model[prefix][token] += 1
        return model, stats


model, stats = fcm(words("sample.txt"), order)

print('MODEL', model)
print('STATS', stats)



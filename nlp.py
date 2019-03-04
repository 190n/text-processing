"""
Removes all words from input that are not uniquely common in that input
"""

import math
import spacy

nlp = spacy.load('en_core_web_md')
nlp.max_length = 1500000

# doc = nlp(open('ootp.txt', encoding='cp1252').read())
doc = nlp(open('python-tutorial.md').read())

logProbs = [(item.text, item.prob) for item in doc]

logProbs.sort(key=lambda i: i[1])

n = math.floor(len(doc) / 2)
frequent = [item[0] for item in logProbs[:n]]

for item in doc:
    if item.text in frequent:
        print(item.text, end=' ')

print('')

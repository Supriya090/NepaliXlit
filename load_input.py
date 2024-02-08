import sys
import re

line = sys.argv[1]
line = re.sub(r'[^a-zA-Z ]+', '', line.strip().lower())

words = line.split(' ')

input_words = []

for word in words:
    input_words.append(' '.join(list(word)))

with open('source/source.txt', 'w') as file:
    for word in (input_words):
        file.write(word + "\n")
import re
from collections import Counter

def words(text):
    """
    Extracts all words from the given text
    """
    return re.findall(r'\w+', text.lower())

def train(features):
    """
    Builds a frequency table of words from the given text
    """
    model = Counter(features)
    return model

def levenshtein_distance(s1, s2):
    """
    Computes the Levenshtein distance between two given strings
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1], distances[index1 + 1], newDistances[-1])))
        distances = newDistances
    return distances[-1]

def spell_check(word, model):
    """
    Spell checker function that checks if the given word is spelled correctly
    """
    max_distance = 2
    suggested_words = []
    for candidate in model:
        distance = levenshtein_distance(word, candidate)
        if distance <= max_distance:
            suggested_words.append(candidate)
    return suggested_words

if __name__ == '__main__':
    text = "This is a sample text to train our spell checker. The spell checker will be able to detect the mistakess in the text."
    WORDS = train(words(text))
    word = 'mistakess'
    print(spell_check(word, WORDS))

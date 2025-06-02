import random

words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled"],
    "adjective": ["small", "great", "fuzzy", "funny", "light"],
    "preposition": ["through", "over", "under", "beyond", "across"],
    "adverb": ["barely", "mostly", "easily", "already", "just"],
    "color": ["pink", "blue", "mauve", "red", "transparent"],
    "name": ["eliza", "jenny", "beatrice", "robert", "aaron"],
    "name's": ["eliza's", "jenny's", "beatrice's", "robert's", "aaron's"],
}

templates = ["""
    Yesterday the color noun
    verb preposition coach name
    adjective color noun that was
    adverb adjective before
    """,
    
    """
    Tomorrow the color noun
    verb preposition coach name's
    adjective color noun that was
    adverb adjective after
    """, 

    """Today the color noun
    verb preposition coach name's
    adjective color noun that was
    adverb adjective now
    """, 
]


def random_sentence():
    sentence = []
    for token in templates[random.randint(0,2)].split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


def random_paragraph():
    for _ in range(random.randint(3, 9)):
        print(random_sentence(), end=" ")

    
random_paragraph()

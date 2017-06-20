"""
Create random non-boring twitter messages.
"""

import random

nouns=["Tromso", "Norway", "Git", "GitHub", "This workshop"]
verbs=["is", "was"]
adverbs=["very", "actually", "really", "completely", "rather", "a bit"]
adjectives=["amazing", "rainy", "sunny", "interesting", "mind-blowing", "HUGE"]
punctuations=['.', '...', '!', ';']

def tweet():
    return ' '.join([random.choice(nouns),
                     random.choice(verbs),
                     random.choice(adverbs),
                     random.choice(adjectives)]) \
                     +random.choice(punctuations)

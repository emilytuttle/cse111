
# Creativity: I added an adjective into the sentence with a get_adjective function.

import random

def main():

    def get_determiner(quantity):
        if quantity == 1:
            words = ["A", "One", "The"]
        else:
            words = ["Some", "Many", "The"]

        determiner = random.choice(words)
        return determiner
    
    def get_adjective():
        words = ["red", "blue", "green", "big", "pretty",
        "ugly", "long", "mean", "angry", "happy",
        "large", "tiny", "amazing", "rude", "sweet",]
        adjective = random.choice(words)
        return adjective

    def get_noun(quantity):
        if quantity == 1:
            words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        else:
            words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        word = random.choice(words)
        return word

    def get_verb(quantity, tense):
        if tense == 'past':
            words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
            verb = random.choice(words)
            return verb
        elif tense == 'present' and quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
            verb = random.choice(words)
            return verb
        elif tense == 'present' and quantity != 1:
            words = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
            verb = random.choice(words)
            return verb
        elif tense == 'future':
            words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
            verb = random.choice(words)

            return verb
    def get_preposition():
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        preposition = random.choice(words)
        return preposition
    
    def get_prepositional_phrase(quantity):
        """Build and return a prepositional phrase composed
        of three words: a preposition, a determiner, and a
        noun by calling the get_preposition, get_determiner,
        and get_noun functions.

        Parameter
            quantity: an integer that determines if the
                determiner and noun in the prepositional
                phrase returned from this function should
                be single or pluaral.
        Return: a prepositional phrase.
        """
        preposition = get_preposition()
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        adjective = get_adjective()
        return [preposition, determiner, noun, adjective]

        
        

  

    def make_sentence(quantity, tense):
        determiner = get_determiner(quantity)
        adjective = get_adjective()
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        phrase = get_prepositional_phrase(quantity)
        print(determiner, adjective, noun, verb, phrase[0], phrase[1].lower(), phrase[3], phrase[2])

    make_sentence(1,'past')
    make_sentence(1,'present')
    make_sentence(1,'future')
    make_sentence(2,'past')
    make_sentence(2,'present')
    make_sentence(2,'future')

main()


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """

    if word not in wordList:
        return False

    word_dict = getFrequencyDict(word)
    
    for key in word_dict.keys():
        if key not in hand.keys():
            return False
        else:
            if word_dict[key] > hand[key]:
                return False

    return True
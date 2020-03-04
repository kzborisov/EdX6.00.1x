'''In this problem set, you'll implement two versions of a wordgame!
Don't be intimidated by the length of this problem set. 
There is a lot of reading, but it can be done with a reasonable amount of thinking and coding. 
It'll be helpful if you start this problem set a few days before it is due!

Let's begin by describing the 6.00 wordgame: 
This game is a lot like Scrabble or Words With Friends, if you've played those.
Letters are dealt to players, who then construct one or more words out of their letters.
Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:
Dealing:
- A player is dealt a hand of n letters chosen at random (assume n=7 for now).
- The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
- Some letters may remain unused (these won't be scored).

Scoring:
- The score for the hand is the sum of the scores for each word formed.
- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
- Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value.
- For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32).
  Be sure to check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

As another example, if n=7 and you make the word 'waybill' on the first try, it would be worth 155 points 
(the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all n letters).

Hints:
You may assume that the input word is always either a string of lowercase letters, or the empty string "".
You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps4a.py. You should not change its value.
Do not assume that there are always 7 letters in a hand! The parameter n is the number of letters required for a bonus score 
(the maximum number of letters in the hand). 
Our goal is to keep the code modular - if you want to try playing your word game with n=10 or n=4, you will be able to do it by simply changing the value of HAND_SIZE!

Testing: If this function is implemented properly, and you run test_ps4a.py, you should see that the test_getWordScore() tests pass.
 Also test your implementation of getWordScore, using some reasonable English words.

'''

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; 
    A is worth 1, 
    B is worth 3, 
    C is worth 3, 
    D is worth 2, 
    E is worth 1, 
    and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    word_length = len(word)

    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    if word_length == n:
        total_score = word_length * score + 50
    else:
        total_score = word_length * score
    return total_score

print(getWordScore("",7))
"""
Pig Latin - Pig Latin is a game of alterations played
on the English language game. To create the Pig Latin
form of an English word the initial consonant sound is
transposed to the end of the word and an ay is affixed
(Ex.: "banana" would yield anana-bay). Read Wikipedia
for more information on rules.
"""

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in ["a","e","i","o","u"]:
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word
else:
    print 'empty'

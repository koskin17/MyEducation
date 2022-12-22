# The string given to your function has had an "egg" inserted directly after each consonant.
# You need to return the string before it became eggcoded.
#
# Example
# unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
# //             "B---eg---in---n---er---"
# Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.

import re

def unscramble_eggs(word):
    return re.sub('egg', '', word)


print(unscramble_eggs("ceggodegge heggeregge")) #, "code here")
print(unscramble_eggs("FeggUNegg KeggATeggA")) #, "FUN KATA")

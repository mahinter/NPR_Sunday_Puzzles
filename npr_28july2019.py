# NPR Sunday Puzzle 28 July 2019
# https://www.npr.org/2019/07/28/745971618/sunday-puzzle-high-cs

# This week's challenge comes from listener Andy Blau, a a magician who performs under the name Zoltan the Adequate.
# He describes the word BEVY as "alphabetically balanced." That is, the first letter, B, is second from the start of the alphabet,
# and the last letter, Y, is second from the end of the alphabet. Similarly, E and V are each fifth from the ends of the alphabet.
# Can you think of a six-letter word related to magic that is similarly balanced?

import csv
input_file = csv.reader(open("/usr/share/dict/words"))

WORD_LEN = 6
ASCII_A_OFFSET = 96

for row in input_file:
    cur_word=row[0].lower()
    if len(cur_word) == WORD_LEN:
        num_balanced=0
        for i in range(0,WORD_LEN // 2):
            if ((ord(cur_word[i]) - ASCII_A_OFFSET) == (ASCII_A_OFFSET + 27 - ord(cur_word[WORD_LEN-1-i]))):
                num_balanced=num_balanced+1
            else:
                break
        if num_balanced==(WORD_LEN // 2):
            print(cur_word)




# Think of a common 5-letter word. If you insert an E after the second letter, you'll get a common 6-letter word. If instead you insert an E after the fourth letter, you'll get another 6-letter word. And if instead you insert an E at the end, you'll get still another 6-letter word. What words are these?

import csv
input_file = csv.reader(open("./words.txt"))

dict_5 = dict()
dict_6_2 = dict()
dict_6_4 = dict()
dict_6_5 = dict()

e_pos =[2,4,5] # 0-based index

WORD_LEN = 6

for row in input_file:
    cur_word=row[0].lower()
    if (len(cur_word) == (WORD_LEN)) and (cur_word[2] == 'e'):
        cur_word2=cur_word[:2]+cur_word[3:]
        dict_6_2[cur_word2] = 1
    if (len(cur_word) == (WORD_LEN)) and (cur_word[4] == 'e'):
        cur_word2=cur_word[:4]+cur_word[5:]
        dict_6_4[cur_word2] = 1
    if (len(cur_word) == (WORD_LEN)) and (cur_word[5] == 'e'):
        cur_word2=cur_word[:5]
        dict_6_5[cur_word2] = 1     
    if (len(cur_word) == (WORD_LEN-1)):
        dict_5[cur_word] = 1

keys_5 = set(dict_5.keys())
keys_6_2 = set(dict_6_2.keys())
keys_6_4 = set(dict_6_4.keys())
keys_6_5 = set(dict_6_5.keys())


answer = keys_5 & keys_6_2 & keys_6_4 & keys_6_5
print(answer)

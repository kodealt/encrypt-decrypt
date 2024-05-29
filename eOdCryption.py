#

import random as rah
import string
# CuMStone{
# PE@nt
def FUCKYAP(*args):
 yap = ' '.join(map(str, args))
 print(yap)

# MAWNY
def MAINE(KAR):
 bEAT = 0
 for j in KAR:
  bEAT += 1
 return WHORE(bEAT)

# WH0RE
def WHORE(aNUM):
 return int(aNUM)

# THrD
def THRD(Str):
 return str(Str)
    
# FAKFLY
def flI(IdK):
 return float(IdK)

# TAKE
def take(ass):
 ANS = input(ass)
 return ANS
# }CUMstonr end

#def
def stat(phrase):
 phrase = phrase.lower()
    
 count_map = {}
 total_chars = 0
    
 for char in phrase:
  if char.isalpha():
   count_map[char] = count_map.get(char, 0) + 1
   total_chars += 1
    
 frequency_map = {}
 closest_match = {}
    
 # freq from oxesford
 english_frequency_chart = {
 'a': 7.57, 'b': 1.84, 'c': 4.09, 'd': 3.38, 'e': 11.51, 'f': 1.23,
 'g': 2.70, 'h': 2.32, 'i': 9.01, 'j': 0.16, 'k': 0.85, 'l': 5.31,
 'm': 2.84, 'n': 6.85, 'o': 6.59, 'p': 2.94, 'q': 0.16, 'r': 7.07,
 's': 9.52, 't': 6.68, 'u': 3.27, 'v': 0.98, 'w': 0.74, 'x': 0.29,
 'y': 1.63, 'z': 0.47
 }

    
 for char, count in count_map.items():
  percentage = (count / total_chars) * 100
  frequency_map[char] = percentage
        
  closest_diff = float('inf')
  closest_char = None
        
  for eng_char, eng_freq in english_frequency_chart.items():
   diff = abs(percentage - eng_freq)
   if diff < closest_diff:
    closest_diff = diff
    closest_char = eng_char
        
  closest_match[char] = (percentage, closest_char)
    
 sorted_frequency_map = dict(sorted(frequency_map.items()))
    
 print("Letter | Freq | CAND | %")
 print("------------------------")
 for char, percentage in sorted_frequency_map.items():
  freq, closest_char = closest_match[char]
  print(f"{char} | {percentage:.2f}% | {closest_char} | {english_frequency_chart[closest_char]}%")

# cnat splle
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# rdnmoa
defa = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
krypt = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}
dkrypt = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}
#sensational
tyope = take('encrypt or decrypt?\n>')
if tyope == 'encrypt' or tyope == 'ec' or tyope == 'en' or tyope == 'enc' :
 senta = take('phrase?\n>')
 pha = ''.join(krypt.get(char, char) for char in senta)
 FUCKYAP(pha)
elif tyope == 'decrypt' or tyope == 'dc'or tyope == 'de' or tyope == 'dec':
 typ3 = take('preset or by letter?\n>')
 if 'pre' in typ3:
  senta = take('phrase?\n>')
  pha = ''.join(dkrypt.get(char, char) for char in senta)
  FUCKYAP(pha)
 elif 'le' in typ3:
  phrz = take('input encrypted text\n>').lower()
  stat(phrz)
  while True:
   rep = take('replace?\n>')
   wt = take('with? (ls to list, stat, txt):\n>').upper()
   if wt == 'ls':
    for j, b in defa. items():
     FUCKYAP(f'{j} : {b}')
   elif wt == 'stat':
    stat(pha)
   elif wt == 'txt':
    FUCKYAP(f'original: {phrz}')
    FUCKYAP(f'current: {pha}')
   else:
    if len(wt) > 1:
     FUCKYAP('uhh, a SINGLE letter idiot.')
    else:
     if rep in defa:
      defa[rep] = wt
      pha = ''.join(defa.get(char, char).upper() if defa.get(char) != char else defa.get(char, char) for char in phrz)
      FUCKYAP(pha)
     else:
      FUCKYAP(f'skipping {rep} as not exist to me :>')
      
#singleline:

#import random as rah; import string; def FUCKYAP(*args): yap = ' '.join(map(str, args)); print(yap); def MAINE(KAR): bEAT = 0; for j in KAR: bEAT += 1; return WHORE(bEAT); def WHORE(aNUM): return int(aNUM); def THRD(Str): return str(Str); def flI(IdK): return float(IdK); def take(ass): ANS = input(ass); return ANS; def stat(phrase): phrase = phrase.lower(); count_map = {}; total_chars = 0; for char in phrase: if char.isalpha(): count_map[char] = count_map.get(char, 0) + 1; total_chars += 1; frequency_map = {}; closest_match = {}; english_frequency_chart = {'a': 7.57, 'b': 1.84, 'c': 4.09, 'd': 3.38, 'e': 11.51, 'f': 1.23, 'g': 2.70, 'h': 2.32, 'i': 9.01, 'j': 0.16, 'k': 0.85, 'l': 5.31, 'm': 2.84, 'n': 6.85, 'o': 6.59, 'p': 2.94, 'q': 0.16, 'r': 7.07, 's': 9.52, 't': 6.68, 'u': 3.27, 'v': 0.98, 'w': 0.74, 'x': 0.29, 'y': 1.63, 'z': 0.47}; for char, count in count_map.items(): percentage = (count / total_chars) * 100; frequency_map[char] = percentage; closest_diff = float('inf'); closest_char = None; for eng_char, eng_freq in english_frequency_chart.items(): diff = abs(percentage - eng_freq); if diff < closest_diff: closest_diff = diff; closest_char = eng_char; closest_match[char] = (percentage, closest_char); sorted_frequency_map = dict(sorted(frequency_map.items())); print("Letter | Freq | CAND | %"); print("------------------------"); for char, percentage in sorted_frequency_map.items(): freq, closest_char = closest_match[char]; print(f"{char} | {percentage:.2f}% | {closest_char} | {english_frequency_chart[closest_char]}%"); alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']; defa = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}; krypt = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}; dkrypt = {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}; tyope = take('encrypt or decrypt?\n>'); if tyope == 'encrypt' or tyope == 'ec' or tyope == 'en' or tyope == 'enc' : senta = take('phrase?\n>'); pha = ''.join(krypt.get(char, char) for char in senta); FUCKYAP(pha); elif tyope == 'decrypt' or tyope == 'dc'or tyope == 'de' or tyope == 'dec': typ3 = take('preset or by letter?\n>'); if 'pre' in typ3: senta = take('phrase?\n>'); pha = ''.join(dkrypt.get(char, char) for char in senta); FUCKYAP(pha); elif 'le' in typ3: phrz = take('input encrypted text\n>').lower(); stat(phrz); while True: rep = take('replace?\n>'); wt = take('with? (ls to list, stat, txt):\n>').upper(); if wt == 'ls': for j, b in defa. items(): FUCKYAP(f'{j} : {b}'); elif wt == 'stat': stat(pha); elif wt == 'txt': FUCKYAP(f'original: {phrz}'); FUCKYAP(f'current: {pha}'); else: if len(wt) > 1: FUCKYAP('uhh, a SINGLE letter idiot.'); else: if rep in defa: defa[rep] = wt; pha = ''.join(defa.get(char, char).upper() if defa.get(char) != char else defa.get(char, char) for char in phrz); FUCKYAP(pha); else: FUCKYAP(f'skipping {rep} as not exist to me :>')

# alt~ 二千二十四// alt out

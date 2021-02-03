"""

Wordplay – Use the file wordlist.txt for this problem. Find the following:
(a) All words ending in ime
(b) All words whose second, third, and fourth letters are ave
(c) How many words contain at least one of the letters r, s, t, l, n, e
(d) The percentage of words that contain at least one of the letters r, s, t, l, n, e
(e) All words with no vowels
(f) All words that contain every vowel
(g) Whether there are more ten-letter words or seven-letter words
(h) The longest word in the list
(i) All palindromes
(j) All words that are words in reverse, like rat and tar.
(k) Same as above, but only print one word out of each pair.
(l) All words that contain double letters next each other like aardvark or book, excluding
words that end in lly
(m) All words that contain a q that isn’t followed by a u
(n) All words that contain zu anywhere in the word
(o) All words that contain ab in multiple places, like habitable
(p) All words with four or more vowels in a row
(q) All words that contain both a z and a w
(r) All words whose first letter is a, third letter is e and fifth letter is i
(s) All two-letter words
(t) All four-letter words that start and end with the same letter
(u) All words that contain at least nine vowels.
(v) All words that contain each of the letters a, b, c, d, e, and f in any order. There may be
other letters in the word. Two examples are backfield and feedback.
(w) All words whose first four and last four letters are the same
(x) All words of the form abcd*dcba, where * is arbitrarily long sequence of letters.
(y) All groups of 5 words, like pat pet pit pot put, where each word is 3 letters, all words share
the same first and last letters, and the middle letter runs through all 5 vowels.
(z) The word that has the most i’s.
"""

file1= open('wordlist.txt','r')
str_data =[line.strip('\n') for line in file1]
#print(str_data)
#a)
answer_a =[]
for i in range(0,len(str_data)):
    if len(str_data[i]) >3:
        if str_data[i][-3:] == "ime":
           answer_a.append(str_data[i])
#print(answer_a)

#b)

answer_b =[]
for i in range(0,len(str_data)):
    if len(str_data[i]) >3:
        if str_data[i][1:2] == "a" and str_data[i][2:3] == "v" and str_data[i][3:4] == "e" :
           answer_b.append(str_data[i])

#print(answer_b)

#c)
# letters =["r", "s", "t", "l", "n", "e"]
# answer_c =[]
# for i in range(0,len(str_data)):
#      for text in letters:
#          if str_data[i] not in answer_c:
#             if text in str_data[i]:
#                answer_c.append(str_data[i])
#print(len(answer_c))
#d)
#print(len(answer_c)/len(str_data) * 100)

#e
vowels =["a","e","i","o","u"]
answer_e =[]
for words in str_data:
    if "a" not in words and "e" not in words and "i" not in words and "o" not in words and "u" not in words:
        answer_e.append(words)

#print(words)

#f
vowels =["a","e","i","o","u"]
answer_f =[]
for words in str_data:
    if "a"  in words and "e"  in words and "i"  in words and "o"  in words and "u"  in words:
        answer_f.append(words)

#print(answer_f)

#g
count_10 = 0
count_7 =0
for word in str_data:
    if len(word) == 10:
        count_10 = count_10 + 1
    if len(word) == 7:
        count_7 = count_7 + 1

    if count_10 > count_7:
        pass
        #print( "There are more 10 Letter Words")
    else:
        #print("There are more seven letter words",count_7)
       pass

#h
all_lenght =[]
for words in str_data:
    length = len(words)
    all_lenght.append(length)
#print(max(all_lenght))
    if length == 23:
        pass
        #print(words)

#j
for word in str_data:
    words = list(reversed(word))
    words = "".join(words)
    if word == words:
        pass
       # print(word)

#k
for word in str_data:
    words = list(reversed(word))
    words = "".join(words)
    if words == "rat" or words == "tat":
       #print(word)
      pass

#l
alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
answer_l=[]
for words in str_data:
    for letter in alphabet:
        if letter*2 in words and words[:-3] != "ily":
            answer_l.append(words)

#print(answer_l)

#m
for words in str_data:
    for i in range(len(words)):
        if words[i]=="q" and words[i+1] !="u":
           # print(words)
           pass

##n
for words in str_data:
     if "zu" in words:
        # print(words)
        pass
#o
count_o =0
answer_xx =[]
for wordz in str_data:
    if "ab" and "ab" in word:
        count_o = count_o + 1
        if count_o == 1:
            #print(word)
             pass

#p

for words in str_data:
    if "aeiou" in words:
        #print(words)
        pass

#q
for words in str_data:
    if "z" in words and "w" in words:
        #print(words)
        pass

#r
for words in str_data:
    if len(words) > 5:
        if words[:1] == "a" and words[2:3] == "e" and words[4:5] == "i":
            #print(words)
            pass

#s
for words in str_data:
    if len(words) == 2:
        #print(words)
        pass

#t

for words in str_data:
    if len(words) == 4:
       if words[:1] == words[-1:]:
                #print(words)
           pass

#u
vowel_u =["a","e","i","o","u"]
count_u = 0
for wordsi in str_data:
    count_u = 0
    for vowel in vowel_u:

        if vowel in wordsi:
            count_u = count_u + 1
            if count_u >= 9:
               #print(wordsi)
                pass
#v



for word in str_data:
    if  "a" in word and "b" in word and "c" in word and "d" in word and "e" in word and "f" in word:
         #print(word)
         pass

#w

for word in str_data:
    if word[:4] == word[4:]:
        #print(word)
        pass







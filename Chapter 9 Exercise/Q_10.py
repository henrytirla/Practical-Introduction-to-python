"""Write a program that has a list of ten words, some of which have repeated letters and some
which don’t. Write a program that picks a random word from the list that does not have any
repeated letters."""
from random import randint
word_list =["henry","laura","gaga","gagayas","monique","marina","thomas","leopold","jackson","abigail"]



listofwords=[]
for i in range(len(word_list)):
    #print(words)
    for j in range(len(word_list[i])):
        #print(word_list[i][j], "----j") #You can use this print statement to understand code
        for k in range(j+1,len(word_list[i])):
           # print(word_list[i][k],"---k")
            
          if word_list[i][j] == word_list[i][k]:
              if word_list[i] not in listofwords:
                  listofwords.append(word_list[i])

##Random Selection not implemented
print(listofwords)






from statistics import mean

mylist = []

for i in range(10):
  score = eval(input(f'Enter Test Score {i+1}: '))
  while score < 0 or score > 100:
    score = eval(input(f'Invalid. Enter Test Score {i+1}: '))
    continue
  mylist.append(score)
  
mylist.sort(reverse = True)
max_score = max(mylist)
min_score = min(mylist)
max2_score = mylist[1]
ave_score = mean(mylist)
ave2_score = mean(mylist[:-2])

print(f'The maximum score was {max_score} and the minimum score was {min_score}.')
print(f'The 2nd largest score was {max2_score}.')
print(f'The average was {ave_score}. The average score with the two lowaest scores dropped is {ave2_score}.')

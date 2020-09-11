# Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].


L =[3,1,4]
M =[1,5,9]
sum_list =[]
def combine(L,M):
 sum =map(lambda x,y: x+y,L,M)

print(list(sum))



            # sum_list.append(sum)
            # print(sum_list)




combine(L,M)
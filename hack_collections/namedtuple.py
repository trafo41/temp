""" Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple. """

# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11

# >>> from collections import namedtuple
# >>> Car = namedtuple('Car','Price Mileage Colour Class')
# >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# >>> print xyz
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# >>> print xyz.Class
# Y



#___________________________________________________________________________________________________________

# n = int(input())
# list1 = input().split()
# z = list1.index('MARKS')
# score = []
# #                                                                        # hahaha
# for i in range(n):
#     j = input().split()
#     score.append(int(j[z]))
# # print(format(sum(score)/n, '.2f'))
# print("{0:.2f}".format(sum(score)/n))


#--------------------------------------------Solution by using namedtuple

# n = int(input())
# list1 = []
# for i in range(n):
#     list1.append(input())

# print(list1)

# m = int(input())
# list2 = []
# for i in range(m):
#     list2.append(input())

# print(list2)
#-------------------------------
# list3 = []  
# for i in list2:
#     for k in list1:
#         if k[1:] == i[1:len(k)]:
#             list1.remove(k)
#             list3.append(k)
#         else:
#             list3.append(' ')
# print(list3)
# for i in list3:
#     print(i)
    #----------------------------------------

# for i in list1:
#     for j in list2:
#         if i[1:] == j[1:len(i)]:
#             print(i)


# j = '+ghfd'
# print(j[1:])
# print(len(j))
# def magic(n):
#     l =[]
#     for i in range(n,0,-1):
#         l2 = []
#         for j in range(i-1):
#             l2.append(1)
#         l2.append(n+1-i)
#         l.append(l2)

#     return l

# def show(n):
#     finallist = []
#     for i in range(n,0,-1):
#         j = magic(i)
#         print(j)
#         if i < n:
#             for k in j:
#                 k.append(n-i)
#                 finallist.append(k)
#         else:
#             for k in j:
#                 finallist.append(k)
#     print(finallist)
    
#     yeah = []
#     for i in finallist:
#         i.sort()
#         yeah.append(i)
#     print(yeah)
#     result = []
#     for i in yeah:
#         if i not in result:
#             result.append(i)
#     for i in result:
#         print(*i)

#-----------------------------------------------------------------------------------------------------------------------------------------
# def magic(n):
#     l =[]
#     for i in range(n,0,-1):
#         l2 = []
#         for _ in range(i-1):
#             l2.append(1)
#         l2.append(n+1-i)
#         l.append(l2)

#     return l

# def show(n):
#     finallist = []
#     for i in range(n,0,-1):
#         j = magic(i)
#         if i < n:
#             for k in j:
#                 k.append(n-i)
#                 finallist.append(k)
#         else:
#             for k in j:
#                 finallist.append(k)
    
#     yeah = []
#     for i in finallist:
#         i.sort()
#         yeah.append(i)

#     result = []
#     for i in yeah:
#         if i not in result:
#             result.append(i)
#     for i in result:
#         print(*i)
    

# n = int(input())
# show(n)
#-----------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime
t = datetime.now()
def findcombinations(arr,index,num,reducedNum):
    if reducedNum < 0:
        return
    if reducedNum == 0:
        for i in range(index):
            print(arr[i], end = ' ')
        print(' ')
        return
    
    prev = 1 if (index == 0) else arr[index  - 1]

    for k in range(prev , num + 1):
        arr[index] = k
        findcombinations(arr,index+1,num,reducedNum-k)

   
num = int(input())
arr = [0]*num
findcombinations(arr,0,num,num)

t2 = datetime.now()
print((t2-t).microseconds)

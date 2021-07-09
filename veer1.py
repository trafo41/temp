0# no_stu  = int(input())
# list1 = [[input(), float(input())] for i in range(no_stu)] 
# #print(list1)

# y = []
# for i in list1:
#     y.append(i[1])

# #print(y)
# y.sort(reverse=False)


# a = y[1]
# faulters = []
# for i in list1:
#     if i[1] == a:
#        faulters.append(i[0])

# done1 = sorted(faulters)
# for i in done1:
#     print(i)


# count = []
# def findp(p):
#     for i in p:
#         if i == i[::-1]:
#             print(i,end=' ')
#             count.append(len(i))                                 #  don't what is happening here
#     print()                                
#     return count

#----------------------------------------------------------------------------------------------------------
# v = 'acbcdfe'
v = 'aaaabbbc'
n = len(v)
# new = []
# for len in range(2,n+1):
#     for i in range(n-len+1):
#         j = i+len-1
#         s = ''
#         for k in range(i,j+1):
#             s+=v[k]
#         new.append(s)

new = [ v[i:j+1] for i in range(n) for j in range(i,n) if len(v[i:j+1]) > 1 ]

# new = ['aa', 'aa', 'aa', 'ab', 'bb', 'bb', 'bc', 'aaa', 'aaa', 'aab', 'abb', 'bbb',
# 'bbc', 'aaaa', 'aaab', 'aabb', 'abbb', 'bbbc', 'aaaab','aaabb', 'aabbb',
# 'abbbc', 'aaaabb', 'aaabbb', 'aabbbc', 'aaaabbb', 'aaabbbc', 'aaaabbbc']



# setl = set(new)
# dct = {}
# print(setl)
# for i in setl:
#     z = len(set(i))
#     dct[i] = z
# print(dct)
# count = 0
# vb = []
# for i,j in dct.items():
#     if len(i)%j == 0:
#         vb.append([i,j])
#         if len(i)>count:
#             count = len(i)

# print(count)
# print(max(count))



#----------------------------------------------------------------------------------------------------------
# events = [('abc','12x'),('abc','13x'),('abc','14x'),('14x','abc'),('13x','abd'),('12x','abc')]
# result = []

# for i in events:
#     h = events.index(i)+1
#     for j in events[h:]:
#         # if i[0] == j[1] and i[1] == j[0]:
#         if i == j[::-1]:
#             result.append(j)
# result.sort(key = lambda x : events.index(x))
# print(result)

#                            _______________________OR____________________________
# lst1 = []
# lst2 = []
# for i,j in events:
#     lst1.append(i)
#     lst2.append(j)

# lst3 = []
# for i in range(len(events)):
#     if lst1[i] not in lst3 or lst2[i] not in lst3:
#         lst3.append(lst1[i])
#         lst3.append(lst2[i])
    # else:
    #     c = events.index(i)
    #     break

# for i in events:
#     if i[0] not in lst3 or i[1] not in lst3:
#         lst3.append(i[0])
#         lst3.append(i[1])
#     else:
#         c = events.index(i)
#         break

# for i in events:
#     if i[0] not in lst3:
#         lst3.append(i[1])
#     else:
#         c = events.index(i)
#         break

# print(c)
# result = []
# employees = events[:c]
# employers = events[c:]
# for i in employers:                                              # or events[:c] yaha bhi slicing kr skte h
#     for j in employees:
#         if i[0] == j[1] and i[1] == j[0]:
#             result.append(i)
# print(result)

#----------------------------------------------------------------------------------------------------------
# i = 0
# count = 0
# lst = [(2,12),(4,13),(16,18),(6,10),(3,15),(19,20),(4,6)]
# a = lst[0][0]
# while(i<len(lst)):
#     if a < lst[i][0]:
#         b = lst[i][0] - a
#         if b >1:
#             count += b
#         a = lst[i][1]
#         i += 1
#     elif a < lst[i][1]:
#         a = lst[i][1]
#         i += 1
#     else:
#         i += 1
    
# print(count)


#--------------------------------------------- New-----------------------------------------------
# 
# i = 1
# count = 1000
lst = [(2,12),(4,13),(16,18),(6,10),(3,15),(19,20),(4,6)]
# # lst = [(1,2),(7,8),(13,14),(19,20),(25,26)]
# # lst = [(4,15),(4,8),(9,18)]
# a = lst[0][1]
# while(i<len(lst)-1):
#     if a < lst[i][0]:
#         b = lst[i][0] - a
#         if b > 1 :
#             count = b-1
#         a = lst[i][1]
#         i += 1
#     else :
#         # a < lst[i][1]:
#         a = lst[i][1]
#         i += 1
    
# if count == 1000:
#     print('0')
# else:
#     print(count)


    #                            _____________________________OR _______________________________
from operator import itemgetter

lst.sort(key = itemgetter(0))
print(lst)

# i = 1
# x = lst[0][1]
# while(i<len(lst)-1):
#     if x < lst[i][0]



#----------------------------------------------------------------------------------------------------------

def findp(v):
#     lst = list(v[i:j+1] for i in range(len(v)) for j in range(i,len(v)) if len(v[i:1+j]) > 1)
    lst = v
    # n = len(lst)//2

    # n = len(v)
    # new = []
    # for x in range(2,n+1):
    #     for i in range(n-x+1):
    #         j = i+x-1
    #         s = ''
    #         for k in range(i,j+1):
    #             s+=v[k]
    #         new.append(s)
                # print(v[k],end='')
#     lst.sort(key = len)
#     print(lst)

    flag = False
    for i in lst:
        print(i)
        if i == i[::-1]:
            print(lst.index(i))
            flag = True
            break
   
    if flag:
        return 'Yes'
    else:
        return 'No'

# from itertools import co
# v = 'hackerrank'
# lst = list(v[i:j+1] for i in range(len(v)) for j in range(i,len(v)) if len(v[i:1+j]) > 1 and len(v[i:1+j]) < 4)
# lst.sort(key = len)
# print(lst)
# print(findp(lst))
# pos = [5,0,9]
# ch = ['z','c','z']
# ans =[]
# for i in range(3):
#     a = v[pos[i]]
#     v = v.replace(a,ch[i],1)
#     lst = list(v[i:j+1] for i in range(len(v)) for j in range(i,len(v)) if len(v[i:1+j]) > 1)
#     lst.sort(key = len)
#     ans.append(findp(lst))
#     print(lst)
# print(ans)




#--------------------------------------------------------------------------------------------------------

dfa = 'acbcdfe'
jk = []

newl = [ dfa[i:j+1] for i in range(n) for j in range(i,n) if len(dfa[i:j+1]) > 1 ]
print(newl)
# for i in newl:
#     print(len(set(i)), end = ' ')
#     if len(i) % len(set(i)) == 0:
#         # jk.append([i,len(i)])
#         jk.append(len(i))
# so = max(jk)
# print()

# print(max(jk))

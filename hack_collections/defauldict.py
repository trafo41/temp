#                                                             # use appending in dict
# # from collections import defaultdict

# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# print(d)
# for i in d.items():
#     print(i)

# result :  ('python', ['awesome', 'language'])
#           ('something-else', ['not relevant'])

#-------------------------------------------------------------------------------------

# from collections import defaultdict

# n, m = map(int, input().split())
# d = defaultdict(lambda: -1)

# for i in range(1, n+1): 
#     word = input()
#     d[word] = d[word] + ' ' + str(i) if word in d else str(i)                             # bit advanced

# print(d)

# for _ in range(m):
#     print(d[input()])

#_____________________________________________________________OR_______________________________________________

from collections import defaultdict
n , m = map(int,input().split())

A = [input() for i in range(n)]
B = [input() for i in range(m)]

d = defaultdict(list)
for i in range(len(A)):
    d[A[i]].append(str(i+1))
for i in B:
    if i in A:
        print(' '.join(d[i]))
    else:
        print(-1)

#_____________________________________________________________explanation_______________________________________________

# # Inputs
# # ------
# n, m = map(int, input().split(' '))

# # Let's get the groups as lists
# # -----------------------------
# #input1 = ['a', 'a', 'b', 'a', 'b']
# #input2 = ['a', 'b']
# input1 = list()
# for i in range(n):
#     input1.append(input())

#     input2 = list()
# for i in range(m):
#     input2.append(input())

# # Calculate Output
# # ----------------
# d = defaultdict(list)

# # Fill d with input1 values
# for i in range(n):
#     d[input1[i]].append(i+1)
# #print(d) --> defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# # Apply the logic for printing
# for i in input2:    
#     if i in d:
#         print(*d[i])
#     else:
#         print(-1)

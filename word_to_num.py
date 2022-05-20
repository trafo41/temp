list1 = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

word = list(input("\nEnter a word : ").upper())
print("\n",*word, sep='  ')                         # *word instead of using join and all

nums = []
sum = 0
for i in word:
    if i in list1:
        nums.append(list1.index(i))
        sum  = sum + list1.index(i)
    

print(nums)
print('-'*len(word)*3 + "------")
print("Numerical value : ", sum)

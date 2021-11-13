# a=int(input("enter any number"))
# for i in range(1,a):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print("")
# for i in range(1,a):
#     b=1
#     for j in range(a,0,-1):
#         if j>i:
#             print("",end="")
#         else:
#             print(b,end="")
#             b+=1
#     print("")
# for i in range(0,a+1):
#     for j in range(a-i,0,-1):
#         print(j,end="")
#     print("")    

# n="MISSISSIPPI"
# a=[]
# for i in n:
#     if i not in a:
#         a.append(i)
# for i in range(0,len(a)):
#     count=0
#     for j in range(0,len(n)):
#         if a[i]==n[j]:
#             count+=1
#     print(a[i],"=",count)
# 
# count = {"M":0,"I":0,"S":0,"P":0}
# word = "MISSISSIPPI"
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	elif i == "P":
# 		count['P'] = count['P']+1
# print (count)               


# dic={}
# a="mississippi"
# count1=1
# count2=1
# count3=1
# count4=1
# for i in a:
#     name='m'
#     if(i=='m'):
#         dic[name]=count1
#         count1=count1+1
#     name='i'
#     if(i=='i'):
#         dic[name]=count2
#         count2=count2+1
#     name='s'
#     if(i=='s'):
#         dic[name]=count3
#         count3=count3+1
#     name='p'
#     if(i=='p'):
#         dic[name]=count4
#         count4=count4+1
# for m in sorted(dic.values()):
#     print(m,":",dic[m])


# word = 'mississippi' 
# for letter in set(word):
#     print(letter, '=', word.count(letter))

# s=input()
# for  i in range(len(s)):
#     if s[i] not in s[:i]:
#         print(s[i]+"="+s.count(s[i]))

# word = "mississippi"
# counter = {}
# for letter in word:
#     if letter not in counter:
#         counter[letter] = 0
#     counter[letter] += 1
# print(counter)
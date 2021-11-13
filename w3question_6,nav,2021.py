# (21) Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# d = {'1':['a','b'], '2':['c','d']}
# a,b = d.values()
# for i in a:
#     for j in b:
#         print(i+j)
# d={'1':['a','b'], '2':['c','d']}
# for i in d['1']:
#     for j in d['2']:
#         r=i+j
#         print(r)
# (22) Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
# dic1 = {'a':23,'b':32,'c':37,'d':50,'e':76,'f':65}
# a = []
# for i in dic1.values():
#     a.append(i)
# a.sort()
# print(a[:-4:-1])

# (23)Write a Python program to combine values in python list of dictionaries.

# # t={ [{'item': 'item1', 'amount': 400},{'item': 'item2', 'amount': 300},
# # {'item': 'item1', 'amount': 750}]}
# # r = {}
# # for i in t:
# #     k = i['item']
# # v = i['amount']
# # if k not in r.keys():
# #     t1 = {k:v}
# #     r.update(t1)
# # else:
# #     r[k] += v
# # print(r)
# t=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# s={}
# for i in t:
#     if i['item'] in s.keys():
#         s[i['item']]+=i['amount']
#     else:
#         s[i['item']]=i['amount']
# print(s)

# (24) Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'

# string = 'w3resource'
# # d = {}
# # for i in string:
# #     if i not in d:
# #         d[i] = 1
# #     else:
# #         d[i] += 1
# # print(d)
# dict1 = {}
# for i in string:
#     dict1[i] = string.count(c)
# print (dict1)

# (25)Write a Python program to print a dictionary in table format.
# d = {'a':[1,2,3],'b':[5,6,7],'c':[9,10,11]}
# print(*d.keys())
# a=(list(d.values()))
# for i in range(len(a)):
#     print(*a[i])

# (26)Write a Python program to count the values associated with key in a dictionary.
# (27)Write a Python program to convert a list into a nested dictionary of keys.
# (28)Write a Python program to sort a list alphabetically in a dictionary.
# (29)Write a Python program to remove spaces from dictionary keys.
# (30)Write a Python program to get the top three items in a shop.
# a={'item1':45.50,'item2':35,'item3':41.30,'item4':55,'item5':24}
# for i in a:
#     print(a[i])

# (31)Write a Python program to get the key, value and item in a dictionary.
# d={'y':23,'o':4,'u':6,'m':8}
# c=d.values()
# d1=d.keys()
# for i in c,d1:
#     print(*i)

# (32)Write a Python program to print a dictionary line by line.
# d={'Alex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
# for x,y in d.items():
# #     print (x)
# for i,j in d.items():
#     print (i," : ",j)

# (33)Write a Python program to check multiple keys exists in a dictionary.
# d= {'n': 'Alex', 'c': 'V', 'r_d': '2'}
# if len(d) >1:
#     print("true")
# else:
#     print("false")

# (34) Write a Python program to count number of items in a dictionary value that is a list.
# k={'u':7,'y':9,'s':6,'n':2,'t':4}
# # print(len(k))
# count=0
# for i, j in k.items():
#     count+=1
#     # print(k[i])
#     print(count)

# (35) Write a Python program to sort Counter by value. 
# d = {'Math':81, 'Physics':83, 'Chemistry':87}
# l = sorted(d.values())
# r = []
# for i in l[:: -1]:
#     for k, v in d.items():
#         if i == v:
#             r.append((k, v))
# print(r)

# (36)Write a Python program to create a dictionary from two lists without losing duplicate values.
# l1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
# l2 = [1, 2, 2, 3]
# d = {}
# for i in range(len(l1)):
#     if l1[i] not in d:
#         d[l1[i]] = {l2[i]}
#     elif l1[i] in d:
#         d.update({l1[i]:{l2[i]}})
#     else:
#         print("try its")
# print(d)

# (37)Write a Python program to replace dictionary values with their average.
# l= [{'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
# {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
# {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}]
# for i in l:
#     a = i.pop("id")
# i["id"]= a
# n1 = i.pop('V')
# n2 = i.pop('VI')
# i['V+VI'] = (n1 + n2)/2
# print(l)

# (38)Write a Python program to match key values in two dictionaries.
# d1 = {'key1': 1, 'key2': 3, 'key3': 2}
# d2 = {'key1': 1, 'key2': 2}
# for i in d1.items():
#     for j in d2.items():
#         if i == j:
#             print()
# print(i[0], ":", j[1], " is present in both i and j")

# (39)Write a Python program to store a given dictionary in a json file.
# (40)Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
# d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
#    'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
#    'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# for i,j in d.items():
#     print(j[4])
# for i in d:
#     print(i,'its value',d[i])

# (41)Write a Python program to drop empty Items from a given Dictionary.
# a={'c1': 'Red', 'c2': 'Green', 'c3': None}
# x={}
# for k, v in a.items():
#     if v!=None:
#         x[k]=v
# print(x)

# (42)Write a Python program to filter a dictionary based on values.
# d1={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# d2= {}
# for i,j in d1.items():
#     if j > 170:
#         d2[i] = j
# print(d2)

# (43) Write a Python program to convert more than one list to nested dictionary.
# l1 = ['S001', 'S002', 'S003', 'S004']
# l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3 = [85, 98, 89, 92]

# (44)Write a Python program to filter the height and width of students, which are stored in a dictionary. Go to the editor
# d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# for i in d:
#     print(i)

# (45)Write a Python program to check all values are same in a dictionary. Go to the editor
# d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# # print(all(c==12 for c in d.values()))
# for i in d.values():
#     if i==12:
#         continue
# print(all("True"))

# (46)Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
# L = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = {}
# for i in L:
#     if i[0] not in d.keys():
#         d.update({i[0]:[i[1]]})
#     elif i[0] in d.keys():
#         d[i[0]].append(i[1])
# print(d)

# (47)Write a Python program to split a given dictionary of lists into list of dictionaries.
# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# r=[]
# a,c=d.values()
# for i in range(len(a)):
#     for j,k in d.items():
#         b=({j:k[i]})
#         r.append(b)
# print(r)

# (48)Write a Python program to remove a specified dictionary from a given list.
# d=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# d1 = []
# for i in d:
#     if (i['id'] not in '#FF0000'):
#         d1.append(i)
# print(d1)

# (49)Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
# l=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# a,b=l
# a1={}
# a2={}
# final_list=[]
# for i,j in a.items():
#     d={i:int(j)}
#     a1.update(d)
# for i,j in b.items():   
#         d1={i:int(j)}
#         a2.update(d1)
#         final_a=a1,a2
# for i in final_a:
#     final_list.append(i)
# print(final_list)

# (50)A Python Dictionary contains List as value. Write a Python program to clear the list values in the said dictionary.
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3' : [12, 34]}
# for i in d.keys():
#     d[i]=[]
# print(d)

# (51)A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
# d={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# c=[]
# for i in d:
#     for j in d:
#         if len(d) and i==j:
#             if i is not c:
#                 c.append(j)
#         else:
#             c.append(i)
# print(c)
     

# (52)Write a Python program to extract a list of values from a given list of dictionaries.
# d=[{'Math': 90, 'Science': 92},{'Math': 89, 'Science': 94},{'Math': 92, 'Science': 88}]
# c=[]
# for i in d:
#     c.append(i['Science'])
# print(c)


# (53)Write a Python program to find the length of a given dictionary values.
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# c=len(d)
# print(c)
# # for i in d:
# #     print(i)
# b={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# a=len(b)
# print(a)
# # for i in b:
# #     print(i,b[i]) 

# (54)Write a Python program to get the depth of a dictionary. 
# d = {'a':1, 'b': {'c': {'d':{'u':3}}}}
# count = 0
# for x in str(d):
#     if x == '}':
#         count += 1
# print(count)

# (55)Write a Python program to access dictionary key's element by index.
# d={ 'Physics':3,'Math': 4,'Chemistry':2}
# for i in d:
#     print(i)#.index(i))

# (56)Write a Python program to convert a given dictionary into a list of lists.
# d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# print([[i,j] for i,j in d.items()])
# m={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# print([[i,j] for i,j in m.items()])

# (57)Write a Python program to filter even numbers from a given dictionary values.
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for k in d.keys():
#     d[k] = [i for i in d[k] if i%2 ==0]
# print(d)  
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for k in d.keys():
#     for j in d[k]:
#         if j%2==0:
#             print([j])
# b={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# for j in b.keys():
#     b[j] = [i for i in b[j] if i%2 ==0]
# print(b) 

# (58)Write a Python program to get all combinations of key-value pairs in a given dictionary.
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in range(len(d)):
#     for j,i in d.items():
#         print(d[j])
# b={'V': [1, 3, 5], 'VI': [1, 5]}
# for i in range(len(b)):
#     for j,i in b.items():
#         print(b[j])

# (59)Write a Python program to find the specified number of maximum values in a given dictionary.
# d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# j=[]
# for i in d:
#     j.append(i[::-1])
# print(j)
# d = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24,'f': 100, 'g': 57, 'h': 8, 'i': 100}
# d_s = sorted(d.items(),key=lambda k: k[1],reverse=True)
# print([d_s[1][0]])
# print( [ k for k,v in d_s[0:2]])
# print( [ k for k,v in d_s[0:5]])


# l=[1,2,3,[4,5,6],[7,8,9],10,11,12]
# for i in l:
#     if type(i) == list:
#         print(l.index(i))

# l=[1,2,3,[4,5,6],[7,8,9],10,11,12,[13,14,15]]
# for i in l:
#     if type(i) == list:
#         print(l.index(i))

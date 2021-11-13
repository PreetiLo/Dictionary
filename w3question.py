# (1)write a python script to sort (ascending and descending ) a dictionary by value.
# d={"h":2,"y":5,"u":3,"r":6,"w":4,"b":1}
# l=[]
# d1={}
# for y in d.values():
#     l.append(y)
#     l.sort()
# for y in l:
#     for x in d:
#         if d[x] == y:
#             d1.update({x:y})
# print(d1)

# (2) write a python script to add a key to a dictionary.
# a={0:10,1:20}
# a[2] = 30
# print(a) 
# o/p {0:10,1:20,2:30}

## print(len(input("enter any thing")))
## print(len([1,2,3,4]))
## a=-6
## b=2
##print(a//b)

# (3) write a python script to concatenate follwing dictionaries to create a new one.

# dic0={}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic0 = dic1, dic2, dic3
# print(dic0)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# (4) write a python script to check whether a given key already exists in a dictionary.
# n=int(input("enter the key:"))
# a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# if n in a:
#     print("Its key present")
# else:
#     print("Its key is not present")



# (5) Write a Python program to iterate over dictionaries using for loops.
# a={0:10,1:20,3:30,4:40}
# for x,y in a.items():
#     print(x,"=",y)

# (6) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# a=int(input("Input a number "))
# d = dict()
# for i in range(1,a+1):
#     d[i]=i*i
# print(d) 

# (7)  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# a=dict()
# for i in range(1,55):
#     a[i]=i*i
# print(a)
# a=dict()
# i=1
# while i<55:
#     a[i]=i*i
#     i+=1
# print(a)

# (8) Write a Python script to merge two Python dictionaries.
# a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# b={"h":2,"y":5,"u":3,"r":6,"w":4,"b":1}
## b.update(a)
## print(b)
# for i in a:
#     b.update({i:a[i]})
# print(b)

# (9) Write a Python program to iterate over dictionaries using for loops.
# a={"t":50,"u":30,"w":60,"v":40,"s":20,"x":10}
#a={"preeti":1,"pooja":2,"subreena":3,"piya":5}
# b=[]
# c={}
# for x,y in a.items():
#    print(x,"=",y)
# for x in a.values():
#     b.append(x)
#     b.sort()
# for y in b:
#     for x in a:
#         if a[x] == y:
#             c.update({x:y})
# print(c)


# (10) Write a Python program to sum all the items in a dictionary. 
## d={"u":2,"y":3,"t":4,"h":5}
# d={0:10,2:30,1:40,3:60,4:20}
# sum=0
# for i in d:
#     sum=sum+d[i]
#     sum=sum+i
#     print(sum)

# (11) Write a Python program to multiply all the items in a dictionary.
# d={0:9,2:5,1:7,3:8,4:10}
# c=2
# for i in d:
#     c=c*d[i]
#     print(c)

# (12) Write a Python program to remove a key from a dictionary. 
# t= {'m':1,'u':2,'p':3,'s':4,'w':5}
# del t['p']
# print(t)
# if 'p' != t: 
#     del t['p']
# print(t)

# (13) Write a Python program to map two lists into a dictionary. 
# k= ['preeti', 'komal', 'anjali']
# v = [2,5, 8]
# # # c= dict(zip(k,v))
# c = []
# d={}
# for i in range(len(k)):
#     c.append((k[i],v[i]))
#     # d.update(c)
# print(dict(c))
# # print(d)

# (14) Write a Python program to sort a given dictionary by key.
# d={'g':7,'l':12,'h':8,'d':4,'e':5,'i':9,'a':1,'c':3,'f':6,'j':10,'k':11,'b':2}
# c=[]
# c1={}
# for i in d.values():
#     c.append(i)
#     c.sort()
# for j in c:
#     for i in d:
#         if d[i] == j:
#             c1.update({i:j})
# print(c1)

# (15) Write a Python program to get the maximum and minimum value in a dictionary.
# d=dict()
# n=int(input("Enter a number of entries: "))
# for i in range(1,n):
#     x = int(input("Enter a number: "))
#     d[x]=x
# print("Maximum of values is: ",(max(d.values())))
# # print("Minimum of values is: ",(min(d.values())))

# (16) Write a Python program to get a dictionary from an object's fields.
# d={}

# (17) Write a Python program to remove duplicates from Dictionary.
# b={"nav":4,"kul":8,"guru":12,"nav":5,"guru":10,"kul":15}
# for i in b:
#     print(i,b[i])
# d1={}
# for i,j in b.items():
#     if j is not d1.values():
#         d1[i]=j
# print (d1)

# (18) Write a Python program to check a dictionary is empty or not.
# d={}
# if not d:
#     print("empty")
# else:
#     print("not empty")

# (19) Write a Python program to combine two dictionary adding values for common keys
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# # for i,j in d1.items():
# #     for i1,j1 in d2.items():
# #         if i==i1:
# #             d1[i]=j+j1
# # print (d1)
# d3={}
# for x in d1.keys():
#     if x in d2.keys():
#         d1[x]=d1[x]+d2[x]
#         d2.pop(x)
#         for d in (d1,d2):
#             d3.update(d)
# print(d3)

# (20) Write a Python program to print all unique values in a dictionary.
# d1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# l1=[]
# for i in d1:
#     for x,y in i.items():
#         if y not in l1:
#             l1.append(y)
# print (l1)



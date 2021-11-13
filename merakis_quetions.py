# city_population = {"NewYorkCity":8550405,"LosAngeles":3971883, "Toronto":2731571, 
#     "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, 
#     "Vancouver":631486, "Boston":667137 }
# # print(city_population["NewYorkCity"])
# # print(city_population)
# # print(type(city_population))
# # for i in city_population:
# #     print(i,"=",city_population[i])
# for i in range(1,len(city_population)):
#     print(i)

# Dict = {'ball' : 'green','Ball': 'red' }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# person={'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)


# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

# dic= {

#     'Name': 'RAM',

#     'Age': 17,

#      }

# dic['student']={

#         'id':22, 

#         'place':'dharamsala'

#     }

# print(dic)

# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.")

# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# # mydict=classes.copy()
# # print(mydict)
# print(classes)

# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# # person.popitem()
# del person('place')
# print(person)

# iteration 

# states_capitals = {
#     'Gujarat' : 'Gandhinagar',
#     'Maharashtra' : 'Mumbai',
#     'Rajasthan' : 'Jaipur',
#     'Bihar' : 'Patna'
#     }
# for state in states_capitals:
#     print(state)
#     print(states_capitals[state])

# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# # for x in details.values():
# for x,y in details.items():
#     print(x,y)

# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# # for i in range(0,len(meal)):
# #     print(i)
# print(len(meal))

# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }
# print(details["name"])
# # print(details["lastname"])
# print(details["age"])

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1
# print(sum)

# c=dict()
# for i in range(1,16):
#     c=i*i
#     print(c) 

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)

# dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#           3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#         }
#     }
# for i in dic:
#     print(i,dic[i])
# # print(dic)

# li=["one","two","three","four","five"]
# l=[1,2,3,4,5,] 
# c={}
# for i in (li,l):
#     c.update(i)
#     print(c)

ruit = {}


# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 

# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)

box = {}

jars = {}

crates = {}

box['biscuit'] = 1

box['cake'] = 3

jars['jam'] = 4

crates['box'] = box

crates['jars'] = jars

print (len(crates[box]))
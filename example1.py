#----------------------------------------------------Day-1---------------------------------------------------------------

# print("hello world","dsfdfs")

# name = "something"
# age = 1
# gender = "male"

# print(name,age,gender)

# if 1:
#         print("this is if")

list1=['1',"8",'3']

# print(list1[4])

# list1.efruittend(['1',333,444])
# print(list1)
# list1.append("some value")
# print(list1)
# list1.remove("some value")
# print(list1)



# for a in list1:
#                 print(a)

# list1.reverse()
# print(list1)

# list1.sort(reverse=True)
# print(list1)

# fruit = ["orange","bana"]

# if "apple" in fruit:
#                 print("apple is included in fruit")
# else:
#     print("apple is not in fruit")

# x=[1,2,3,4,5]

# def isEven(no):
#     if (no % 2 == 0):
#             return no

# filterdList= filter(isEven,x)

# print(list(filterdList))

#--------------------------------------------------------Day-2------------------------------------------------------------

tuple1=('apple','orange','mango')

# print(tuple1)

# print(tuple1[0])
# print(tuple1[1:2])

# print(tuple1.count("orange"))
# print(tuple1.index("apple",0,3))
# print(len(tuple1))

tupleToList=list(tuple1)
# print(tupleToList)
tupleToList.append("new value")
# print(tupleToList)
# age=input("Enter your age:")

# print("your age is",age)
# print("type of age",type(age))
# print("type of age after type casting",type(int(age)))

# grade={
#     "student1":80,
#     "student2":70,
#     "student3":60,
# }
# for key,value in grade.items():
#     print(key,":",value)

# grade['student4']=90

# print(grade)

# if int(input("enter your age:")) >= 18:
#     print("you must serve in military")
# else:
#     print("you must not serve in military")

# temperatureType=input("Choose temperature type-\n1.Farenheit\n2.Centigrade\nEnter option no:")

# if int(temperatureType) <1 or int(temperatureType)>2:
#     print("invalid option")
#     exit()

# temperature=input("Enter temperature:")

# def convertToFarenheit():
#     farenheit=(int(temperature) * 1.8)+32
#     print(farenheit,"F")

# def converToCentigrade():
#     centigrade=(int(temperature)-32)/1.8
#     print(centigrade,"C")

# operation=convertToFarenheit if int(temperatureType) == 1 else converToCentigrade
# operation()

for i in range(1,11,2):
    print(i )



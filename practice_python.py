# # file = open("history.txt", "r")
# file = open("history.txt", "w")
# content = file.write("Let's go.\n Have a nice day!")
# #line = file.readline()
# #lines = file.readlines()
# print(content)
# file.close()

# fruits = ["apple", "banana", "cherry", "orange"]

# for x in fruits:
#     print(x)


# number = [1,2,3,4,5,6,7,8,9,10]
# for i in number:
#     print(i)


# count = 0
# while count < 5:
#     print(count)
#     count += 1


# for i in range(5):
#     if i == 3:
#         continue
#     print(i)


# a = float(input("Enter first number:"))
# print("User entered number:", a)

AQI = int(input("Enter your AQI score: "))

if AQI <= 40:
    print("You are living in good environment.")
elif AQI <=80:
    print("You are living in moderate environment.")
elif AQI <=120:
    print("You are living in unhealthy environment.")
elif AQI <=200:
    print("You are living in very unhealthy environment.")
else:
    print("You are living inside Smoke/Fog City environment.")

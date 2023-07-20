import random

randomList = []

# generate list with random integers between 10 and 50
def method1(len):
    for i in range(len):
        randomList.append(random.randint(10,50))
    return randomList

# sum elements of the list
def method2(randomList):
    return sum(randomList)

while True:
    userNumber = input("Enter number between 5 and 15 ")

    try:
        userNumber = int(userNumber)
        if userNumber >= 5 and userNumber <= 15:
            break
        else:
            print("Please Enter a Valid Number")
    except ValueError:
        print("Please Enter a Valid Number")

list = method1(userNumber)
sum = method2(randomList)

print("The elements of the array are:" + str(randomList))
print("The sum of the array is: " + str(sum))

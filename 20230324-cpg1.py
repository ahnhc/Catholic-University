# sum from 1 to 10

# i = 1
# sum = 0
# while i <= 10:
#     sum+=i
#     i+=1
# print("sum = ",sum)

# While statement with else

# i = 0
# while i < 3:
#     print(i,"Inside a loop")
#     i+=1
# else:
#     print("else part")

# Sum up nums as many as you want

# total = 0
# answer = "y"
#
# while answer == "y":
#     number = int(input("enter the number : "))
#     total+=number
#     answer = input("continue? (y / n) : ")
# print(f"Total sum is : {total}")

# exercise : math test

# import random
# Flag = True
# score = 0
# while Flag:
#     x = random.randint(1,100)
#     y = random.randint(1,100)
#     answer = int(input(f"{x} + {y} = "))
#     if answer == x+y:
#         print("Correct!")
#         score+=1
#     else:
#         print("Wrong!")
#         Flag = False
#         print(f"Your score is {score}")

# exercise : login program

# password = ""
# while password != "python is fun":
#     password = input("Enter your password : ")
# print("Login Successfully!")

# exercise : guessing random number

# import random
# flag = True
# failed = 0
# number = random.randint(1, 10)
# while flag:
#     entered = int(input("Enter your guess(number): "))
#     if number < entered:
#         print("Down!")
#         failed += 1
#     elif number > entered:
#         print("Up!")
#         failed+=1
#     else:
#         print(f"Congratulation. The # of attempts = {failed}")
#         print(f"The answer is {number}")
#         Flag = False
#         number = random.randint(1, 10)
#         failed = 0

# Nested loops
# for i in [1,2,3]:
#     print("Welcome to Programming Class!")
#     for i in [1,2]:
#         print("Hi! " *i)

# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print("")

# end="" 명령어를 사용하면 print 되는 값을 한 줄에 붙여서 출력하게 해준다.

# print("All cases where the sum of the dice is 6")
# for i in range(1,6):
#     for j in range(1,6):
#         if i+j ==6:
#             print(f"1st dice : {i} 2nd dice : {j}")

# exercise : Multiplication table

# for i in range(1,10):
#     for j in range(1,10):
#         k = i*j
#         print(f"{i} * {j} = {k}")

# infinite loop and break & continue

# for i in range(1, 11):
#     print(i, end="")
#     if i == 7:
#         break

# print("### Who's in front of me ###")
# name = input("Enter the name : ")
# wait_list = ['Emma','Angela','Helena','Nicole','Elizabeth','Tina']
# for i in wait_list:
#     print(i, end=" ")
#     if i == name:
#         break

# exercise : color of traffic light

# while True:
#     light = input('Enter the color of traffic light (red/yellow/green): ')
#     if light == 'green':
#         break
# print( 'Go!!')

# exercise : times table test

num_list = []
answer = 'y'
while answer == 'y':
    nums = int(input("Which times table do you test? (Enter nums btw 2 and 9) : "))
    num_list.append(nums)
    answer = str(input("More?(y/n) : "))
print(f"We will test {num_list} times table.")

exam_list = []
while i in range(num_list):
    exam = random.randint(1, 10)
    exam_list.append(exam)
    i+=1

problems = 3*range(num_list)
print(f"We will test {problems} problems.")

while j in range(num_list):
    print(f"{num_list[j]} * {exam_list[j]} = {}")
    j+=1
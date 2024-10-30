# while loop = execute some code WHILE some condition remains true
# iteration = loops

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     # name = input("Enter your name: ")

# # This is what is called an "Infinite Loop"

# else:
#     print(f"Hello {name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cant be negative")
#     age = int(input("Enter your age: "))

# else: 
#     print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# else:
#     print("Bye")


# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))

# else:
#     print(f"Your number is {num}")

###### FOR LOOPS

# for loops = execute a block of code a fixed number of times.
#   You can iterate over a range string, sequence, ect.

# credit_card = "12234-12244-22398-32482"

# for x in credit_cared:
#     print(x)

# for x in range(1, 21):
#     if x == 13:
#         continue #skips over the 13   break stops the program before 13 (12)
#     else:
#         print(x)

########Challenge
# list_of_names =['John', 'Paul', 'George', 'Ringo']
# #If the name is 'George', print "George was found!"
# # othewrwise, print "George was not found!" and print
# # out the other names using a loop

# for name in list_of_names:
#     if name == 'George':
#         print('George was found!')
#     else:
#         print('George was not found!')
#         print(name)

# list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
# #loop through the list_of_names2 and
# #if the name is 'Ironman', skip over it and 
# # print out the other names

# for name in list_of_names2:
#     if name == 'Ironman':
#         continue
#     print(name)

# for name in list_of_names2:
#     if name == 'Thanos':
#         name = 'Black Widow'
#     print(name)
# #This renames Thanos to Black Widow
#     #This is more complicated, but the same

# for i in range(len(list_of_names2)):
#     if list_of_names2[i] == 'Thanos':
#         list_of_names2[i] = 'Black Widow'
#     print(list_of_names2[i])
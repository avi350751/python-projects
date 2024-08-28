# fruits = ['peach','apple','pineapple','guava']
# for i in fruits:
#     print(i)
#     print(i + " pie")
#     if i == 'apple':
#         print("Scream!! No fruits")

# student_scores = [152,45,67,78,90,23,345,1000,67,89,9,56,543,456,56,666,899,989,99]
# total_score = sum(student_scores)
# sorted_score = sorted(student_scores,reverse=True)
# print(total_score)
# print(sorted_score[0])

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score) 

# #Use of range
# x_sum = sum(range(0,6))
# #0+1+2+3+4+5=15
# print(x_sum)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

print('Welcome to password generator: ')
no_of_letters = int(input('How many letters do you want?\n'))
no_of_numbers = int(input('How many numbers do you want?\n'))
no_of_symbols = int(input('How many symbols do you want?\n'))

#Easy Level
# password = ""
# for char in range(1, (no_of_letters + 1)):
#     password += random.choice(letters)

# for char in range(1, (no_of_numbers + 1)):
#     password += random.choice(numbers)

# for char in range(1, (no_of_symbols + 1)):
#     password += random.choice(symbols)

# print(password)

#Hard Level
password_list = []
for char in range(1, (no_of_letters + 1)):
    password_list.append(random.choice(letters))

for char in range(1, (no_of_numbers + 1)):
    password_list.append(random.choice(numbers))

for char in range(1, (no_of_symbols + 1)):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password_new = ""
for char in password_list:
    password_new += char
print(f"Your password is: ",password_new)

                  
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '#' ,'$' ,'*', '%', '&', '<', '>', '+']
numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcom to the pypassword Generator!")
in_letters = int(input("how many letters would you like in your password?\n"))
in_symbols = int(input ("how many symbols would you like?\n"))
in_numbers = int(input ("how many numbers would you like?\n"))

# Easy level
# password =""

# for char in range(0, in_letters):
#     password += (random.choice(letters))

# for sym in range(0, in_symbols):
#      password += (random.choice(symbols))

# for num in range(0, in_numbers):
#      password += (random.choice(numbers))

# print(password)


# HARD password
password_list =[]

for char in range(0, in_letters):
    password_list.append (random.choice(letters))

for sym in range(0, in_symbols):
     password_list.append(random.choice(symbols))

for num in range(0, in_numbers):
     password_list.append (random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password =""
for char in password_list:
    password += char

print(f" Your password is {password}")

print('  Password Generator v1.0  \n')
print('     Made By zitrus2k \n')


import random
import string

print('Do you want any special words in the Password?')
password_w = input('Enter : ')

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password

print('How long should your Password be?')
len_input = int(input('Enter : '))

if len_input == 0:
    print('ERROR 01x '
          'your Password is 0!')


password = generate_password(len_input)
print("Your generated password is:", password + '_' + password_w)

print()
print('-Zitrus Studios Development-')
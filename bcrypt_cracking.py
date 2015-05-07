import bcrypt
import threading

database_file = open('database.txt')
common_passwords = open('commonpasswords.txt')
found = False

database = []

for line in database_file:
    database.append(line.strip().split()[2])
current = 0
for line in common_passwords:
    password = line.strip().encode()
    current += 1
    print(current)
    for user_hash in database:
        temp_hash = str(user_hash).encode()
        if bcrypt.hashpw(password, temp_hash) == temp_hash:
            print('Found answer: ' + user_hash + ' = ' + line.strip())
            exit()

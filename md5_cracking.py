import hashlib

m = hashlib.md5
answer = '531081da76633a6e27318745fab6e45e'
wordlist = []
first_word = 0
second_word = 1
test_number = 0
found = False

words = open('wordlist.txt')

for line in words:
     wordlist.append(line.strip())

for first_word in wordlist:
     if found:
          break
     for second_word in wordlist:
          current_test = first_word + second_word
          if hashlib.md5(current_test.encode('utf-8')).hexdigest() == answer:
               print('Answer: ' + current_test)
               found = True
               break

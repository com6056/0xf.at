dictionary = open('latindictionary.txt')
dictionary_list = []
answer = ''

for term in dictionary:
    dictionary_list.append(term.strip())

paragraph = input('Paste paragraph here: ')
words = paragraph.split()
current_word = 0
for word in words:
    words[current_word] = word.lower()
    if word[-1] == '.':
        words[current_word] = word[:len(word) - 1].lower()
    current_word += 1

for word in words:
    if word in dictionary_list:
        pass
    else:
        current_letter = 0
        for letter in word:
            temp_list = list(word)
            temp_list[current_letter] = chr(ord(temp_list[current_letter]) - 1)
            if ''.join(temp_list) in dictionary_list:
                print(word + ' ' + ''.join(temp_list))
                answer += chr(ord(temp_list[current_letter]))
                break
            else:
                current_letter += 1
print(answer)
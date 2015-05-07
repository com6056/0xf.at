dictionary = open('dictionary.txt')

scrambled_words = input('Enter scrambled words: ')

scrambled_words = scrambled_words.split(';')

answer = ''

for word in scrambled_words:
    dictionary.seek(0, 0)
    sorted_scrambled_word = sorted(word)
    for line in dictionary:
        sorted_word = sorted(line.strip())
        current_char = 0
        for char in sorted_word:
            if char == sorted_scrambled_word[current_char]:
                if current_char < len(sorted_scrambled_word) - 1:
                    current_char += 1
                elif len(sorted_scrambled_word) != len(line.strip()):
                    break
                else:
                    answer = answer + line.strip() + ';'
                    break
            else:
                break

print(answer)
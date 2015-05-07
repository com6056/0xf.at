nums = [22, 222, 2222, 33, 333, 3333, 44, 444, 4444, 55, 555, 5555, 66, 666, 6666, 77, 777, 7777, 77777, 88, 888, 8888, 99, 999, 9999, 99999]
code = input('Enter code: ')
total = 0
for char in code:
    if char.isdigit():
        total += int(char)
    else:
        conversion = nums[ord(char) - 97]
        for num in str(conversion):
            total += int(num)
print(total)
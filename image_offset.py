from PIL import Image

answer = ''
image = Image.open('image_offset.png')
picture = image.load()
(width, height) = image.size
for y in range(height):
    for x in range(width):
        if picture[x, y] != 0:
            answer += chr(x + 65)
print 'Answer: {}'.format(answer)

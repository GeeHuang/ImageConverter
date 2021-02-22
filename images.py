from PIL import Image, ImageFilter

img = Image.open('Pokedex/pikachu.jpg')
filter_img = img.convert('L')
box = (100,100,400,400)
resized = filter_img.crop(box)
resized.save('grey.png','png')
resized.show()

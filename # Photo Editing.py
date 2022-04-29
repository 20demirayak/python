# Photo Editing 
# pip install pillow
from PIL import Image, ImageFilter
# Resize an image
img = Image.open('img.jpg')
resize = img.resize((200, 300))
resize.save('output.jpg')
# Blur Image
img = Image.open('img.jpg')
blur = img.filter(ImageFilter.BLUR)
blur.save('output.jpg')
# Sharp Image
img = Image.open('img.jpg')
sharp = img.filter(ImageFilter.SHARPEN)
sharp.save('output.jpg')
# Crop Image
img = Image.open('img.jpg')
crop = img.crop((0, 0, 50, 50))
crop.save('output.jpg')
# Rotate Image
img = Image.open('img.jpg')
rotate = img.rotate(90)
rotate.save('output.jpg')
# Flip Image
img = Image.open('img.jpg')
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip.save('output.jpg')
# Transpose Image
img = Image.open('img.jpg')
transpose = img.transpose(Image.TRANSPOSE)
transpose.save('output.jpg')
# Convert Image to GreyScale
img = Image.open('img.jpg')
convert = img.convert('L')
convert.save('output.jpg')
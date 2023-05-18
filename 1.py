from PIL import Image

#_Box (left, upper, right, lower)

im = Image.open('postcard.jpg')
im_crop = im.crop((10, 200, 600,500))
im_crop.save('cropped_postcard.jpg', quality=95)
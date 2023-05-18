from PIL import Image, ImageDraw, ImageFont


name = input("Введите имя получателя: ")
filename = "postcard.jpg"
with Image.open(filename) as img:
    img.load()
font = ImageFont.truetype("PlayfairDisplay-Italic-VariableFont_wght.ttf", 55)
draw_text = ImageDraw.Draw(img)
draw_text.text(
    (img.width // 2 - 100, 15),
    name + ", поздравляю!",
    font=font,
    fill=('#FF0000')
)
img.show()
img.save(name + "_postcard.png")
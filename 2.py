from PIL import Image
d = {1: "newyear.jpg", 2: "23feb.jpg", 3: "8mart.jpg", 4: "bd.jpg"}

print("1 - Новый год\n"
      "2 - 23 февраля\n"
      "3 - 8 марта\n"
      "4 - День рождения")
ans = int(input("Для получения открытки введите число - номер прадника : "))

filename = d[ans]
with Image.open(filename) as img:
    img.load()

img.show()

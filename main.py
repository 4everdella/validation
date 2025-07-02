import re
phone = input(" Telefon raqam kiriting: ")

number = r'^\+\d{12}$'

if re.fullmatch(number, phone):
    print("Raqam to‘g‘ri")
else:
    print(" Noto‘g‘ri  12 ta raqam bo‘lishi kerak")
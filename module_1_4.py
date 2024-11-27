from asyncio import current_task

my_string = input("Введите произвольный текст: ")
print("Длина текста =", len(my_string), "символов")
print("В верхнем регистре:", str.upper(my_string))
print("В нижнем регистре:", str.lower(my_string))
my_string = my_string.replace(" ","")
print("Текст без пробелов:", my_string.replace(" ",""))
print("Первый символ строки my_string:",my_string[0])
print("Последний символ строки my_string:",my_string[-1])
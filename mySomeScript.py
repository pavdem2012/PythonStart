# Вывод
# в консоль

name = 'Darling'  # Объявляем переменную name

print("Hello,", name, '!!!!')  # Вывод в консоль

print(2 + 3)  # Вывод в консоль

print("Ups. Come on")  # Вывод в консоль
# TODO: непонятно что это и как
# но похоже очень прикольно и нужно
a = 1  # Объявляем переменную a
print("Дана переменная а = ", a)  # Выводим в консоль переменную a
print("Идентификатор переменной a = ", id(a))   # Выводим идентификатор переменной
b = 2  # Объявляем переменную b
print("Дана переменная b = ", b)  # Выводим в консоль переменную b
print("Идентификатор переменной b = ", id(b))   # Выводим идентификатор переменной
# FIXME: еще одна непонятная классная штука
if a > b:  # Сравниваем перменные
    print("Yes a < b")  # Вывод в консоль
else:
    print("No a < b")  # Вывод в консоль

a = b
print("Идентификатор переменной a = ", id(a))   # Выводим идентификатор переменной

c = (1, 3, 5)  # Объявляем переменную c

print("Тип переменной name - ",type(name))  # Вывод в консоль типа переменной
print("Тип переменной name - ",type(a))  # Вывод в консоль типа переменной
print("Тип переменной name - ",type(c))  # Вывод в консоль типа переменной

numList = [1, 2, 3, 4, 5]  # Объявляем переменную numList список чисел
print("Объявленый список numList", numList)   # Выводим список в консоль
print("Идентификатор переменной numList = ", id(numList))   # Выводим идентификатор переменной
numList[2] = 8  # Изменяем значение третьего элемента
print("Измененный список = ", numList)   # Выводим список в консоль
print("Идентификатор переменной numList = ", id(numList))   # Выводим идентификатор переменной


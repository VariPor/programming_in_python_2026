"""
Пользователь вводит числа, большие 0, 
критерий окончания ввода – число 0. 
Вывести наибольшее среди всех чисел.
"""
max_num = 0 
while True:
    num = int(input())
    if num < 0:
        print(f"{num} < 0 - ошибка")
        break
    if num == 0:
        break
    max_num = max(num, max_num)    
print(f"Максимальное введённое число {max_num}")
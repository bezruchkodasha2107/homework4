numbers = input("Введите три числа через пробел: ")

a = numbers.split()
sum_of_numbers = sum(map(int, a)) 

print(f"Сумма чисел = {sum_of_numbers}")
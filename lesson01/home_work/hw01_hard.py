
__author__ = 'Салахетдинов Шамиль'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)
a = float("inf")
print('a = float("inf")')
print('----------------')
print(f"a == a**2 => {a == a**2}")
print(f"a == a*2 => {a == a*2}")
print(f"a > 999999 => {a > 999999}")


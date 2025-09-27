def gcd(a, b):
    old_r, r = a, b     #Начальные остатки
    old_s, s = 1, 0     #Коэффициенты Безу для a
    old_t, t = 0, 1     #Коэффициенты Безу для b
    while r != 0:
        whole = old_r // r       #Целая часть от деления
        old_r, r = r, old_r - whole * r      #Обновляем остатки
        old_s, s = s, old_s - whole * s      #Обновляем коэффициенты Безу
        old_t, t = t, old_t - whole * t
    return old_r, old_s, old_t


a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
nod, x, y = gcd(a, b)
print('Нод =', nod)
print(f"{a}*{x} + {b}*{y} = {nod}")
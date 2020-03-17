breaked = []
for x in range (1,500):
    if x % 3 == 0:
        breaked.append(x)
        continue
    elif x % 5 == 0:
        breaked.append(x)
        continue
    elif x % 11 == 0:
        breaked.append(x)
        continue
    elif x % 13 == 0:
        breaked.append(x)
        continue
    elif (x + 17) % 15 == 0 :
        breaked.append(x)
        continue
    elif x % 17 > 0.73 :
        breaked.append(x)
        continue
    print(x)
print(breaked)
for item in breaked:
    if item == 11156:
        print("Есть")
        break
if 11156 in breaked and 1253 in breaked:
    print("Есть")




              


# ''' будет печатать все числа от 1 до 5 млн, кроме: 
# - тех, которые деляться нацело на 3, 5, 11, 13,
# - тех, которые в сумме с 17 деляться нацело на 15,
# - тех, у которых остача от деления на 17 больше 0,73.
# 2. Напечатает все пропущенные значения. Если среди них есть 
# 11156 или 1253, или 157895, или 12556842, или 1225868, 
# или 1256, или 14785 - напечатать "ЕСТЬ" 
# '''
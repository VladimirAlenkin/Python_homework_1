# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
#сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 	Примеры/Тесты:
# 	3 2 4 -> yes
# 	3 2 1 -> no

size1 = int(input("Введите размер долек шоколада по горизонтали: "))
size2 = int(input("Введите размер долек шоколада по вертикали: "))
quantity = int(input("Насколько Вы голодны, сколько долек Вы хотите съесть: "))
print('YES' if quantity%size1 == 0 or quantity%size2 == 0  else 'NO')

#решено

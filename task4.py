f = open("space.txt", encoding='utf8').readlines()  # считываем файл
f.pop(0)  # удаляем первую строку без данных
for i in range(len(f)):  # удаляем '/n' из всех строк
    f[i] = f[i].replace("\n", "")
    f[i] = f[i].split("*")
print(f)
q = []
for i in range(len(f)): # генератор паролей
    passwd1 = f[i][1][-3] + f[i][1][-2] + f[i][1][-1]
    passwd2 = f[i][0][1] + f[i][0][2]
    passwd3 = f[i][1][0] + f[i][1][1] + f[i][1][2]
    passwd = passwd1 + passwd2 + passwd3
    passwd = passwd.casefold().swapcase()#делаем пароль капсом
    p1 = ""
    for i in range(len(passwd)):
        p1 += passwd[len(passwd)-1-i] # переворачиваем пароль
    q.append(p1)
f1 = open("space_uniq_password.csv", 'w')
f1.write("password \n")
for i in range(len(q)):
    f1.write(q[i] + '\n')

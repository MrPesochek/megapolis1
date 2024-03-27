f = open("space.txt", encoding='utf8').readlines() #считываем файл
f.pop(0) # удаляем первую строку без данных
j = []
for i in range(len(f)): #удаляем '/n' из всех строк
    f[i] = f[i].replace("\n", "")
    f[i] = f[i].split("*")
j = ['0'*len(f)]
for i in range(len(f)):
    if f[i][2].split(' ')[0] == '0' or f[i][2].split(' ')[1] == '0':
        #вводим переменные, которые понадобятся в формуле, используя индексы и срезы
        n = int(f[i][0][5])
        m = int(f[i][0][6])
        t = len(f[i][1])
        xd = int(f[i][3].split(' ')[0])
        yd = int(f[i][3].split(' ')[1])
        #вычисляем побитые значения по формуле из условия
        if n > 5:
            x = n + xd
        else:
            x = -1*(n+xd)*4+t
        if m > 3:
            y = m+t+yd
        else:
            y = -1*(n+yd)*m
        #заносим побитые данные в массив
        if f[i][2].split(' ')[0] == '0':
            f[i][2] = str(x) + ' ' + f[i][2].split(' ')[1]
        if f[i][2].split(' ')[1] == '0':
            f[i][2] = f[i][2].split(' ')[0]+ ' ' + str(y)
        if f[i][0][3] == "V":
            for q in range(len(f[i]) - 1):  # добавляем разделители *
                f[i][q] += '*'
            print("".join(f[i]))
#сохраняем данные в файл, восстанавливая исходный вид
with open("space_new.txt", "w") as f1:
    for i in range(len(f)):
        for q in range(len(f[i])-1): #добавляем разделители *
            if f[i][q].__contains__('*'): # проверка на отсутствие разделителя
                pass
            else:
                f[i][q] += '*'
        f1.write("".join(f[i]) + "\n") #сохраняем данные в файл
def find (name):
    f = open("space.txt", encoding='utf8').readlines() #считываем файл
    f.pop(0) # удаляем первую строку без данных
    for i in range(len(f)): #удаляем '/n' из всех строк
        f[i] = f[i].replace("\n", "")
        f[i] = f[i].split("*")
    i = 0
    while i < len(f): #проверка корабля на наличие в списке
        cname = f[i][0]
        if name == cname:
            # задаем переменные planet и direction
            planet = f[i][1]
            direction = f[i][3]
            return f"Корабль {name} был отправлен с планеты: {planet} и его направление движения было: {direction}" # возвращаем строку в нужном нам формате
        i += 1
    return "error.. er.. ror.." # возвращаем строку error.. er.. ror.. т.к. корабля нет в списке
while True:
    q = input() # получаем название корабля
    if q == 'stop': break # при вводе "stop" программа останавливается
    else: print(find(q)) # вызов функции поиска
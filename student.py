f = open('document.txt', "w")

lst = [
    ["Имя Фамилия 1", 20],
    ["Имя Фамилия 2", 25],
    ["Имя Фамилия 3", 19],
	["Имя Фамилия 4", 12],
	["Имя Фамилия 5", 16],
	["Имя Фамилия 6", 34],
	["Имя Фамилия 7", 76],
]
for i in range(0, len(lst), 1):

   print("Имя " + lst[i][0] + " Возраст " + str(lst[i][1]))

   
names = ['Василий', 'Маша', 'Гера']

#       преобразование  - цикл for
st = [ len(a) for a in names if len(a) > 4]

print( st )
x = 10

f = open('document.txt', "w")

f.write(str(x) + '\n' + str(x))
f.close()



print("Вводите строки, если вы хотите закончить ввод, введите пустую строку: \n")
strings = []
while True:
    a = input()
    if a == "":
        break
    strings.append(a)
strings = sorted(strings, key=lambda x: len(x.split(" ")))
for string in strings:
    print(string)
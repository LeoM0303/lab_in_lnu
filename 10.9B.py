N = int(input("Введіть розмір масиву N: "))


array = []

print("Введіть елементи масиву:")

for i in range(N):

    element = int(input(f"Елемент {i + 1}: "))

    array.append(element)


print("Масив у зворотному порядку:")

for elem in reversed(array):

    print(elem)

 

# Crear una funcion que permita ingresar al usuario
#Numero enteros...y strings...
# 1- print -> imprime la lista que se fue cargando hasta el momento...
# 2- append a -> siendo a numero entero
# 3- remove b -> siendo b numero entero
# 4- sort
# 5- reverse
# 6- insert c d -> siendo ambos numeros enteros, c el indice y d el valor
# 7- exit -> termina el programa

isRunning = True

myList = []

while isRunning:

    userInput = input("Ingrese comando: ")
    command =userInput.split()



    if userInput == "exit":
        isRunning = False
    elif command[0] =="append":
        myList.append(int(command[1]))
    elif command[0] == "print":
        print(myList)
    elif command[0] == "sort":
        myList.sort()
    elif command[0] == "insert":
        myList.insert(int(command[1]),int(command[2]))
import json

def contarPares(n):
    contador = 0
    for i in range(n):
        if i % 2 == 0:
            print(i)
            contador.append(i)

    return contador



x = 0

while x < 10:
    x = int(input("Enter a number: "))
    print(x)

    pares = contarPares(x)
    print("Cantidad de numeros pares" + str(pares))

print("Hola Mundo..")

frontend_data = '{ "name":"John", "age":30, "city":"New York"}' 

parsed_data = json.loads(frontend_data)

print(parsed_data)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

json_converter_data = json.dumps(x)

print(json_converter_data)


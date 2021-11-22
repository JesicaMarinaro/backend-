from src.Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.tipo = tipo
        
    def damePrecio(self):
        return self.precio

    
myAlimento = Alimento("Pollo", 10, 10, "Carnes")

print(myAlimento.damePrecio())

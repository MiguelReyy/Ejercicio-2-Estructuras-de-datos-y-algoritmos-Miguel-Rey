# Definición de la clase Punto2D
class Punto2D:
    # Constructor de la clase que inicializa los atributos x e y
    def __init__(self, x, y):
        self.x = x  # Asigna el valor de x al atributo x del objeto
        self.y = y  # Asigna el valor de y al atributo y del objeto
    
    # Método para realizar una traslación del punto en el plano
    def traslacion(self, dx, dy):
        self.x += dx  # Incrementa la coordenada x por dx
        self.y += dy  # Incrementa la coordenada y por dy
    
    # Método especial para representar el objeto como una cadena de caracteres
    def __str__(self):
        return f"X: {self.x}  Y: {self.y}"  # Retorna una cadena formateada con las coordenadas x e y


# Definición de la clase Punto3D, que hereda de Punto2D
class Punto3D(Punto2D):
    # Constructor de la clase que inicializa los atributos x, y, y z
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Llama al constructor de la clase base para inicializar x e y
        self.z = z  # Asigna el valor de z al atributo z del objeto
    
    # Método para realizar una traslación del punto en el espacio tridimensional
    def traslacion(self, dx, dy, dz):
        super().traslacion(dx, dy)  # Llama al método de traslación de la clase base para x e y
        self.z += dz  # Incrementa la coordenada z por dz
    
    # Método especial para representar el objeto como una cadena de caracteres
    def __str__(self):
        return f"X: {self.x}  Y: {self.y}  Z: {self.z}"  # Retorna una cadena formateada con las coordenadas x, y, y z
    


# Ejemplo de uso de la clase Punto2D
a = Punto2D(1, 2)  # Crea un objeto Punto2D con coordenadas (1, 2)
print("A = {}".format(a))  # Imprime las coordenadas del punto creado

a.traslacion(-1, -2)  # Realiza una traslación del punto
print("A = {}".format(a))  # Imprime las nuevas coordenadas del punto tras la traslación

b = Punto2D(-3, 0)  # Crea otro objeto Punto2D con coordenadas (-3, 0)
print("B = {}".format(b))  # Imprime las coordenadas del segundo punto creado
b.traslacion(5, -1)  # Realiza una traslación del punto
print("B = {}".format(b))  # Imprime las nuevas coordenadas del segundo punto tras la traslación


# Ejemplo de uso de la clase Punto3D
c = Punto3D(1, 2, 3)  # Crea un objeto Punto3D con coordenadas (1, 2, 3)
print("C = {}".format(c))  # Imprime las coordenadas del punto creado

c.traslacion(-1, -2, -3)  # Realiza una traslación del punto
print("C = {}".format(c))  # Imprime las nuevas coordenadas del punto tras la traslación

d = Punto3D(-3, 0, 2)  # Crea otro objeto Punto3D con coordenadas (-3, 0, 2)
print("D = {}".format(d))  # Imprime las coordenadas del segundo punto creado

d.traslacion(5, -1, 3)  # Realiza una traslación del punto
print("D = {}".format(d))  # Imprime las nuevas coordenadas del segundo punto tras la traslación

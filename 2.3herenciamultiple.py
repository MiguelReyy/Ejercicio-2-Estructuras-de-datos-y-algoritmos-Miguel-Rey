class A:
    """
    Clase base que inicializa tres atributos a, b y c con los valores proporcionados.
    """

    def __init__(self, a, b, c):
        """
        Inicializa los atributos a, b y c con los valores proporcionados.
        """
        self.a = a
        self.b = b
        self.c = c

class B(A):
    """
    Clase que hereda de A.
    """

    pass

class C(A):
    """
    Clase que hereda de A.
    """

    pass

class D(B, C):
    """
    Clase que hereda de B y C.
    """

    def __init__(self, a, b, c, d=None):
        """
        Inicializa los atributos a, b y c llamando al constructor de la clase base y también inicializa el atributo d.
        """
        super().__init__(a, b, c)
        self.d = d

# Pruebas
d = D(1, 2, 3)  # Instancia de la clase D
# Comprobación de la instancia de D también es instancia de A, B y C
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))  
# Impresión de los valores de los atributos a, b y c de la instancia d
print(d.a, d.b, d.c)

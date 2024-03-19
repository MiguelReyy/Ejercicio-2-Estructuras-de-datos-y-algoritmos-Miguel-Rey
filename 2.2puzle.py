class Base:
    """
    Clase base que define atributos y métodos comunes.
    """

    def __init__(self):
        """
        Inicializa los atributos a, b y c con valores predeterminados.
        """
        self.a = "a"
        self.b = "b"
        self.c = "c"

    def A(self):
        """
        Método para imprimir el valor del atributo a.
        """
        print(self.a)

    def B(self):
        """
        Método para imprimir el valor del atributo b.
        """
        print(self.b)

    def C(self):
        """
        Método para imprimir el valor del atributo c.
        """
        print(self.c)


class Derivada(Base):
    """
    Clase derivada que hereda de Base y modifica algunos atributos y métodos.
    """

    def __init__(self):
        """
        Inicializa los atributos a y c con valores modificados y llama al constructor de la clase base.
        """
        self.a = "aa"
        super().__init__()
        self.c = "cc"

    def A(self):
        """
        Método para imprimir el valor del atributo a (sobrescribe el método en Base).
        """
        print(self.a)

    def B(self):
        """
        Método para modificar el valor del atributo b, llamar al método B de la clase base y luego imprimir el nuevo valor de b.
        """
        self.b = "bb"
        super().B()
        print(self.b)


base = Base()  # Instancia de la clase Base
derivada = Derivada()  # Instancia de la clase Derivada

base.A()  # Imprime 'a'
derivada.A()  # Imprime 'aa' (sobrescritura de método)

print()

base.B()  # Imprime 'b'
derivada.B()  # Modifica y luego imprime 'bb' (sobrescritura parcial de método)

base.C()  # Imprime 'c'
derivada.C()  # Imprime 'cc' (modificación de atributo)

derivada = base  # Asigna la instancia base a derivada
derivada.C()  # Imprime 'c' (el valor de c permanece sin cambios)

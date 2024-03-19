class MuroExterior:
    # Inicializa un MuroExterior con una orientación dada y una lista vacía para las aberturas
    def __init__(self, direccion):
        self.direccion = direccion
        self.aberturas = []

    def agregar_abertura(self, abertura):
        self.aberturas.append(abertura)

    # Calcula la superficie total acristalada del muro sumando las superficies de todas sus aberturas
    def superficie_acristalada(self):
        return sum(abertura.superficie for abertura in self.aberturas)


class MuroCristal(MuroExterior):
    # Inicializa un MuroCristal con una orientación y una superficie total, heredando de MuroExterior
    def __init__(self, direccion, superficie):
        super().__init__(direccion)
        self.superficie_cristal = superficie

    # Devuelve la superficie acristalada total del muro cristal
    def superficie_acristalada(self):
        return self.superficie_cristal


class Abertura:
    # Inicializa una Abertura asignándola a un muro, con una superficie dada y una protección. Si no hay protección, lanza una excepción
    def __init__(self, muro, superficie, proteccion):
        if proteccion is None:
            raise Exception("Se requiere protección")
        self.muro = muro
        self.superficie = superficie
        self.proteccion = proteccion
        muro.agregar_abertura(self)


class Edificio:
    # Inicializa un Edificio con una lista de muros.
    def __init__(self, muros):
        self.muros = muros

    # Calcula y devuelve la superficie acristalada total del edificio sumando las superficies acristaladas de todas sus muros
    def superficie_acristalada(self):
        return sum(muro.superficie_acristalada() for muro in self.muros)


def main():
    # Instanciación de los muros
    muro_norte = MuroExterior("NORTE")
    muro_oeste = MuroExterior("OESTE")
    muro_sur = MuroExterior("SUR")
    muro_este = MuroExterior("ESTE")

    # Instanciación de las aberturas con protección
    abertura_norte = Abertura(muro_norte, 0.5, "Persiana") # ¡IMPORTANTE! Para comprobar que se cumple la excepción, sustituir el valor de protección por "None"
    abertura_oeste = Abertura(muro_oeste, 1, "Persiana")
    abertura_sur = Abertura(muro_sur, 2, "Estor")
    abertura_este = Abertura(muro_este, 1, "Estor")

    # Instanciación del edificio con los 4 muros
    edificio = Edificio([muro_norte, muro_oeste, muro_sur, muro_este])
    print("Superficie acristalada inicial del edificio:", edificio.superficie_acristalada())

    # Reemplazo de un muro por un muro de cristal
    edificio.muros[2] = MuroCristal("SUR", 10)
    print("Superficie acristalada final del edificio:", edificio.superficie_acristalada())

if __name__ == "__main__":
    main()

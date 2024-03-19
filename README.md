# Clases Punto2D y Punto3D

Este proyecto contiene las definiciones de las clases `Punto2D` y `Punto3D`, que representan puntos en un plano bidimensional y tridimensional, respectivamente. Ambas clases proporcionan funcionalidades para realizar traslaciones de puntos en el espacio.

## Funcionalidades

### Clase Punto2D
- **Constructor:** Inicializa un punto en el plano bidimensional con coordenadas (x, y).
- **Traslación:** Permite trasladar el punto en el plano bidimensional sumando valores a sus coordenadas x e y.

### Clase Punto3D
- **Constructor:** Inicializa un punto en el espacio tridimensional con coordenadas (x, y, z), heredando las funcionalidades de la clase `Punto2D`.
- **Traslación:** Permite trasladar el punto en el espacio tridimensional sumando valores a sus coordenadas x, y, y z.

## Ejemplo de Uso

```python
# Ejemplo de uso de la clase Punto2D
a = Punto2D(1, 2)  
print("A = {}".format(a))  
a.traslacion(-1, -2)  
print("A = {}".format(a))  

b = Punto2D(-3, 0)  
print("B = {}".format(b))  
b.traslacion(5, -1)  
print("B = {}".format(b))  

# Ejemplo de uso de la clase Punto3D
c = Punto3D(1, 2, 3)  
print("C = {}".format(c))  
c.traslacion(-1, -2, -3)  
print("C = {}".format(c))  

d = Punto3D(-3, 0, 2)  
print("D = {}".format(d))  
d.traslacion(5, -1, 3)  
print("D = {}".format(d))  

```

# Clases A, B, C y D

Este proyecto contiene las definiciones de las clases `A`, `B`, `C` y `D`, que demuestran la herencia múltiple en Python.

## Clase A

La clase `A` es la clase base que inicializa tres atributos `a`, `b` y `c` con los valores proporcionados.

### Métodos

- **`__init__(self, a, b, c)`:** Inicializa los atributos `a`, `b` y `c` con los valores proporcionados.

## Clase B y Clase C

Las clases `B` y `C` heredan de la clase `A`.

## Clase D

La clase `D` hereda tanto de la clase `B` como de la clase `C`, demostrando la herencia múltiple en Python.

### Métodos

- **`__init__(self, a, b, c, d=None)`:** Inicializa los atributos `a`, `b` y `c` llamando al constructor de la clase base (`A`) y también inicializa el atributo `d`.

## Ejemplo de Uso

```python
# Instancia de la clase D
d = D(1, 2, 3)
# Comprobación de la instancia de D también es instancia de A, B y C
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))  
# Impresión de los valores de los atributos a, b y c de la instancia d
print(d.a, d.b, d.c)
```

## 1. MuroExterior.py

Este código define una clase `MuroExterior` que representa un muro exterior de un edificio. Cada instancia de esta clase tiene una dirección y puede contener aberturas como ventanas o puertas. Las funcionalidades principales son:

- Inicializar un muro exterior con una dirección.
- Agregar aberturas al muro.
- Calcular la superficie total acristalada del muro sumando las superficies de todas las aberturas.

##  2. MuroCristal.py

Esta implementación extiende la funcionalidad de `MuroExterior` con una clase `MuroCristal`, que representa un muro completamente hecho de cristal. La funcionalidad principal de esta clase es:

- Sobrescribir el método para calcular la superficie acristalada, devolviendo la superficie total del cristal en lugar de calcularla a partir de las aberturas.

##  3. Abertura.py

Este código define una clase `Abertura` que representa una abertura (ventana o puerta) en un muro exterior. Cada abertura tiene una superficie y una protección asociada. Las funcionalidades principales son:

- Validar que se proporcione una protección para la abertura.
- Agregar automáticamente la abertura al muro especificado al ser inicializada.

##  4. Edificio.py

En este archivo se encuentra la clase `Edificio`, que modela un edificio compuesto por varios muros exteriores. Las funcionalidades principales son:

- Inicializar un edificio con una lista de muros exteriores.
- Calcular la superficie total acristalada del edificio sumando las superficies acristaladas de todos los muros.

##  Ejecución

Para ejecutar cualquiera de estos códigos, simplemente ejecuta el archivo Python correspondiente. Por ejemplo, para ejecutar `MuroExterior.py`, puedes usar el siguiente comando:

```bash
python MuroExterior.py

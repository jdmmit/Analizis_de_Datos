<!-- filepath: /home/ctrl/git_hub/Analizis_de_Datos/Indice.md -->

🧠 **NumPy Cheat Sheet para Ciencia de Datos**

## 📚 Índice Rápido

- [🤔 ¿Qué es NumPy?](#qué-es-numpy)
- [🛠️ Importar NumPy](#importar-numpy)
- [🧩 Tipos de Arrays](#tipos-de-arrays)
- [🏗️ Creación de Arrays](#creación-de-arrays)
- [🥚 Placeholders Iniciales](#placeholders-iniciales)
- [🧬 Tipos de Datos](#tipos-de-datos)
- [🔍 Inspección de Arrays](#inspección-de-arrays)
- [✂️ Subsetting, Slicing e Indexing](#subsetting-slicing-e-indexing)
- [➕➖ Operaciones Matemáticas](#operaciones-matemáticas)
- [🟰 Comparaciones y Boolean Indexing](#comparaciones-y-boolean-indexing)
- [🧮 Funciones Agregadas](#funciones-agregadas)
- [🧩 Manipulación de Arrays](#manipulación-de-arrays)
- [🪞 Copias y Vistas](#copias-y-vistas)
- [💾 Guardar y Cargar Datos](#guardar-y-cargar-datos)
- [🆘 Ayuda y Recursos](#ayuda-y-recursos)
- [🚩 Tips para Estudiantes](#tips-para-estudiantes)

1. 🤔 ¿Qué es NumPy?

NumPy es la librería principal para computación científica en Python. Permite trabajar con arrays multidimensionales de alto rendimiento y muchas funciones matemáticas.

2. 🛠️ Importar NumPy
   import numpy as np

3. 🧩 Tipos de Arrays
   1D array: Vector
   2D array: Matriz (filas y columnas)
   3D array: Tensor (cubos de datos)

# 1D

a = np.array([1, 2, 3])

# 2D

b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)

# 3D

c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)

4. 🏗️ Creación de Arrays
   a = np.array([1, 2, 3]) # Array 1D
   b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float) # Array 2D
   c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float) # Array 3D

5. 🥚 Placeholders Iniciales
   np.zeros((3, 4)) # Array de ceros
   np.ones((2, 3, 4), dtype=int) # Array de unos
   np.arange(10, 25, 5) # Array con valores espaciados (step)
   np.linspace(0, 2, 9) # Array con valores espaciados (n muestras)
   np.full((2, 2), 7) # Array constante
   np.eye(2) # Matriz identidad 2x2
   np.random.random((2, 2)) # Array con valores aleatorios
   np.empty((3, 2)) # Array vacío (valores aleatorios)

6. 🧬 Tipos de Datos
   np.int64 ➡️ Enteros
   np.float32 ➡️ Flotantes
   np.complex ➡️ Complejos
   np.bool ➡️ Booleanos
   np.object ➡️ Objetos Python
   np.string* ➡️ Strings
   np.unicode* ➡️ Unicode
   a = np.array([1, 2, 3], dtype=np.float32)

7. 🔍 Inspección de Arrays
   a.shape # Dimensiones del array
   len(a) # Longitud del array
   a.ndim # Número de dimensiones
   a.size # Número total de elementos
   a.dtype # Tipo de dato de los elementos
   a.dtype.name # Nombre del tipo de dato
   a.astype(int) # Convertir a otro tipo

8. ✂️ Subsetting, Slicing e Indexing
   Subsetting
   a[2] # Elemento en el índice 2
   b[1, 2] # Elemento fila 1, columna 2

Slicing
a[0:2] # Elementos en índices 0 y 1
b[0:2, 1] # Filas 0 y 1, columna 1
b[:1] # Todos los elementos de la fila 0
a[::-1] # Array invertido

Boolean Indexing
a[a < 2] # Elementos menores a 2

Fancy Indexing
b[[1, 0, 1, 0], [0, 1, 2, 0]] # Selección avanzada

9. ➕➖ Operaciones Matemáticas
   g = a - b # Resta
   np.subtract(a, b) # Resta
   b + a # Suma
   np.add(b, a) # Suma
   a / b # División
   np.divide(a, b) # División
   a \* b # Multiplicación
   np.multiply(a, b) # Multiplicación
   np.exp(b) # Exponencial
   np.sqrt(b) # Raíz cuadrada
   np.sin(a) # Seno
   np.cos(b) # Coseno
   np.log(a) # Logaritmo natural
   e.dot(f) # Producto punto

10. 🟰 Comparaciones y Boolean Indexing
    a == b # Comparación elemento a elemento
    a < 2 # Comparación elemento a elemento
    np.array_equal(a, b) # Comparación de arrays completos

11. 🧮 Funciones Agregadas
    a.sum() # Suma total
    a.min() # Mínimo
    b.max(axis=0) # Máximo por columna
    b.cumsum(axis=1) # Suma acumulada por fila
    a.mean() # Media
    np.median(b) # Mediana
    np.corrcoef(a, b) # Correlación
    np.std(b) # Desviación estándar

12. 🧩 Manipulación de Arrays
    Transponer y Cambiar Forma
    np.transpose(b) # Transponer
    b.T # Transponer
    b.ravel() # Aplanar array
    g.reshape(3, -2) # Cambiar forma

Añadir/Eliminar Elementos
np.append(a, [4, 5]) # Añadir elementos
np.insert(a, 1, 5) # Insertar elemento
np.delete(a, [1]) # Eliminar elemento

Combinar y Dividir Arrays
np.concatenate((a, d), axis=0) # Concatenar
np.vstack((a, b)) # Apilar verticalmente
np.hstack((e, f)) # Apilar horizontalmente
np.split(a, 3) # Dividir array

13. 🪞 Copias y Vistas
    h = a.view() # Vista (mismos datos)
    h = a.copy() # Copia profunda (datos independientes)
    np.copy(a) # Copia

14. 💾 Guardar y Cargar Datos
    Guardar en Disco
    np.save('my_array', a) # Guardar array
    np.savez('array.npz', a, b) # Guardar varios arrays
    np.load('my_array.npy') # Cargar array

Guardar/Cargar Texto
np.savetxt("myarray.txt", a, delimiter=" ") # Guardar como texto
np.loadtxt("myfile.txt") # Cargar desde texto
np.genfromtxt("my_file.csv", delimiter=',') # Cargar CSV

15. 🆘 Ayuda y Recursos
    np.info(np.ndarray.dtype) # Información sobre dtype
    help(np.array) # Ayuda sobre arrays

🚩 Tips para Estudiantes
Usa np.array_equal(a, b) para comparar arrays completos, no solo ==.
Si necesitas arrays grandes y rápidos, usa np.zeros, np.ones o np.empty para inicializarlos.
Para manipular datos de sensores o señales (telecomunicaciones), NumPy es tu mejor amigo por su velocidad y eficiencia.
¡No olvides importar siempre NumPy como np!

¿Te gustaría que agregue ejemplos más avanzados, ejercicios o alguna sección especial? ¡Dímelo y lo personalizo aún más!

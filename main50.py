from PIL import Image
import numpy as np

def convertir_imagen_a_matriz(image_path):
    # Cargar la imagen
    imagen = Image.open(image_path)
		imagen_ancho, imagen_alto = imagen.size
    
    # Convertir la imagen a RGB
    imagen = imagen.convert('RGB')
    
    # Obtener los datos de la imagen como una matriz de numpy
    datos = np.array(imagen)
    
    # Crear un diccionario para almacenar los colores y sus números
    colores = {}
    numero = 1
    
    # Crear una matriz para almacenar los números
    matriz = np.zeros((imagen_alto, imagen_ancho), dtype=int)
    
    # Asignar números a los colores y llenar la matriz
    for i in range(imagen_alto):
        for j in range(imagen_ancho):
            color = tuple(datos[i, j])
            if color not in colores:
                colores[color] = numero
                numero += 1
            matriz[i, j] = colores[color]
    
    return matriz, colores

# Ruta de la imagen
ruta_imagen = 'bandit.png'
ruta_output = 'output50.txt'

# Convertir la imagen a una matriz
matriz, colores = convertir_imagen_a_matriz(ruta_imagen)

# Guardar la matriz en un archivo
with open(ruta_output, 'w', encoding='utf-8') as f:
    for fila in matriz:
        f.write(' '.join(map(str, fila)) + '\n')
    f.write('\n\n')
    for color, numero in colores.items():
        hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
        f.write(f"Número {numero}: Color {hex_color}\n")

# Imprimir la matriz
print("Matriz de Color por Números:")
print(matriz)

# Imprimir la leyenda de colores
print("Leyenda de Colores:")
for color, numero in colores.items():
    print(f"Número {numero}: Color {color}")
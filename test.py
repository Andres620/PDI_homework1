import numpy as np
from PIL import Image

# Supongamos que tienes la matriz RGB llamada 'rgb_matrix' de forma (480, 640, 3)
# y 'a' es el tamaño de la submatriz
original_image = Image.open("test.png")
rgb_matrix = np.array(original_image)
a = 3
rows, cols, _ = rgb_matrix.shape

# Calcula cuántas submatrices habrá en cada dirección
num_submatrices_rows = rows // a
num_submatrices_cols = cols // a

# Inicializar listas para almacenar los promedios por canal
promedios_r = []
promedios_g = []
promedios_b = []

# Recorrer filas de 'a' en 'a'
for i in range(0, rows, a):
    # Recorrer columnas de 'a' en 'a'
    for j in range(0, cols, a):
        # Obtener la submatriz de tamaño 'a x a' en los canales R, G y B
        submatriz = rgb_matrix[i:i+a, j:j+a, :]
        
        # Calcular los promedios de cada canal y agregarlos a las listas
        promedios_r.append(np.mean(submatriz[:,:,0]))
        promedios_g.append(np.mean(submatriz[:,:,1]))
        promedios_b.append(np.mean(submatriz[:,:,2]))

# Imprimir los promedios calculados
i=0
print("Promedios R:", promedios_r[i:i+3])
print("Promedios G:", promedios_g[i:i+3])
print("Promedios B:", promedios_b[i:i+3])


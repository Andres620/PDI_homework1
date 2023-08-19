def average_rgb(matrix_rgb):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    total_pixels = 0

    for row in matrix_rgb:
        for pixel in row:
            r, g, b = pixel
            sum_r += r
            sum_g += g
            sum_b += b
            total_pixels += 1
    
    average_r = round(sum_r / total_pixels)
    average_g = round(sum_g / total_pixels)
    average_b = round(sum_b / total_pixels)

    return average_r, average_g, average_b

# Ejemplo de matriz RGB con números concretos
matriz_rgb_ejemplo = [
    [[91, 95, 42], [81, 89, 38], [93, 105, 48]],
    [[95, 85, 58], [92, 83, 53], [100, 86, 57]],
    [[80, 80, 54], [89, 83, 58], [102, 85, 65]]
]
print("type:", type(matriz_rgb_ejemplo))
# Calcular el promedio de cada componente RGB en la matriz de ejemplo
promedio_r, promedio_g, promedio_b = average_rgb(matriz_rgb_ejemplo)
print("Promedio R:", promedio_r)
print("Promedio G:", promedio_g)
print("Promedio B:", promedio_b)

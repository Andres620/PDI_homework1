#venv hmwk_1
from PIL import Image
import numpy as np

#Redimensionar matriz
def resize_matrix_rgb(image_matrix, a):
    m, n, d = image_matrix.shape
    row_remainder = m % a
    col_remainder = n % a
    
    if row_remainder != 0:
        rows_to_add = a - row_remainder
        image_matrix = np.vstack([image_matrix, np.zeros((rows_to_add, image_matrix.shape[1], d))])
        print(image_matrix.shape)
    
    if col_remainder != 0:
        cols_to_add = a - col_remainder
        image_matrix = np.hstack([image_matrix, np.zeros((image_matrix.shape[0], cols_to_add, d))])
    
    return image_matrix



#sacar promedio matriz
def average_rgb(matrix_rgb, x):
    sum_r = 0
    sum_g = 0
    sum_b = 0
    total_pixels = x*x

    for row in matrix_rgb:
        for pixel in row:
            r, g, b = pixel
            sum_r += r
            sum_g += g
            sum_b += b
    
    average_r = round(sum_r / total_pixels)
    average_g = round(sum_g / total_pixels)
    average_b = round(sum_b / total_pixels)

    return average_r, average_g, average_b

def change_resolution(image, r):
    width, height, _ = image.shape
    for i in range(0, width, r):
        for j in range(0, height, r):
            submatrix = image[i:i+r, j:j+r]
            average = average_rgb(submatrix, r)
            submatrix = np.full((r,r,3), average)
            image[i:i+r, j:j+r] = submatrix
    print("Average Color Array: " , image.shape)
    return image
            





if __name__ == '__main__':
    #Subir una imagen
    original_image = Image.open("lena_std.tif")
    #Obtener el tamaño de la imagen
    width, heigth = original_image.size

    # r es el factor de redimenisonamiento
    r = 4
    
    #Redimensionar matriz RGB
    original_image_rgb = np.array(original_image)
    print("Original Shape: ", original_image_rgb.shape)
    original_image_rgb = resize_matrix_rgb(original_image_rgb, r)
    new_image_rgb = change_resolution(original_image_rgb, r)

    #Reestablecer dimensiones originales
    new_image_rgb = new_image_rgb[:heigth, :width, :]

    #Convertir matriz RGB a imagen
    new_image = Image.fromarray(new_image_rgb.astype('uint8'))

    #guardar imagen
    new_image.save("result_test.tif")
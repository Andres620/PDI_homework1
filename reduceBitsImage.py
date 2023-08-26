import numpy as np
from PIL import Image

def reduce_bits(image, n_bits):
    rgb_matrix = np.array(image)
    if n_bits <= 8:
        num_levels = 2 ** n_bits # Cantidad de niveles
        ranges = np.linspace(0, 256, num_levels + 1, dtype="int") #rangos
        levels = np.linspace(0, 255, num_levels, dtype="int") #listad e niveles
        # Aplicar la cuantización a cada canal RGB
        for i in range(3):  # Iterar sobre los canales R, G y B
            result = np.digitize(rgb_matrix[:, :, i], ranges) - 1
            rgb_matrix[:, :, i] = levels[result]
    # Creacion de la imagen modificada
    modified_image = Image.fromarray(rgb_matrix.astype('uint8'))
    return modified_image



if __name__ == '__main__':
    image = Image.open('lena_std.tif')
    n_bits = 1  # Cantiadad de bits
    modified_image = reduce_bits(image, n_bits)
    
    # Save the modified image
    modified_image.save('modified_image.tif')


#El algoritmo está funcionanado pero no esta haciendo bien los rangos
#es decir, para 2 bits deberia mapear valores de 0 y de 255 no de 0 y 1 como lo hace actualmente
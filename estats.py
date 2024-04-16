import random

random.seed(42)

def generar_dades(num_files):
    dades = []
    idx_uno = random.randint(0, num_files - 1)  # Índice para la fila que tendrá el valor 1
    for i in range(num_files):
        if i == idx_uno:
            valor = 1
        else:
            valor = 0
        dades.append(str(valor))  # Convertimos el valor a cadena de texto y lo añadimos a la lista
    print(dades)
    return dades

# Funció per escriure les dades en un fitxer
def escriure_fitxer(dades, nom_fitxer):
    with open(nom_fitxer, 'w') as file:
        for valor in dades:
            file.write(valor + '\n')  # Escrivim cada valor seguit d'un salt de línia

# Nombre de files que vols generar
num_files = 100

# Generar les dades aleatòries
dades_generades = generar_dades(num_files)

# Especifica el nom del fitxer de sortida
nom_fitxer = 'dades_estat.img'

# Escriure les dades en un fitxer
escriure_fitxer(dades_generades, nom_fitxer)

print(f"S'han generat les dades aleatòries i s'han guardat en el fitxer: {nom_fitxer}")
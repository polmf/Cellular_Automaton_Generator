import random

random.seed(42)

def generar_dades(num_files):
    dades = []
    idx_uno = random.randint(0, num_files - 1)  # Índex per la fila que tindrà el valor 1
    for i in range(num_files):
        if i == idx_uno:
            valor = 1
        else:
            valor = 0
        dades.append(str(valor))  # Convertim el valor a cadena de text i l'afegim a la llista
    return dades

# Funció per escriure les dades en un fitxer
def escriure_fitxer(dades, nom_fitxer):
    with open(nom_fitxer, 'w') as file:
        for valor in dades:
            file.write(valor + '\n')  # Escrivim cada valor seguit d'un salt de línia

# Nombre de files que generem
num_files = 100

dades_generades = generar_dades(num_files)

nom_fitxer = 'dades_estat.img'

escriure_fitxer(dades_generades, nom_fitxer)

print(f"S'han generat les dades aleatòries i s'han guardat en el fitxer: {nom_fitxer}")